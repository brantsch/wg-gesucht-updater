#!/usr/bin/env python3

import argparse
import getpass
import time
import pdb

import requests
from bs4 import BeautifulSoup


class WGGesuchtSession(requests.Session):

    def login(self, user, password):
        """ Log in to wg-gesucht.de. Return a new session. """
        url = "https://www.wg-gesucht.de/ajax/sessions.php?action=login"
        data = {"login_email_username": user,
                "login_password": password,
                "login_form_autologin": "1",
                "display_language": "en"}
        res = self.get("https://www.wg-gesucht.de")
        res = self.post(url, json=data)
        print('login', res)
        response = self.get("https://www.wg-gesucht.de/meine-anzeigen.html")
        soup = BeautifulSoup(response.text, features="html.parser")
        nodes = soup.select("a.logout_button")

        self.csrf_token = nodes[0]['data-csrf_token']
        nodes = soup.select("a.logout_button")
        self.user_id = nodes[0]['data-user_id']

    def toggle_activation(self, ad_id):
        """ Deactivate and immediately re-activate the offer. """
        api_url = "https://www.wg-gesucht.de/api/requests/{}/users/{}".format(ad_id, self.user_id)
        headers = {"X-User-ID": self.user_id,
                   "X-Client-ID": "wg_desktop_website",
                   "X-Authorization": "Bearer " + self.cookies.get("X-Access-Token"),
                   "X-Dev-Ref-No": self.cookies.get("X-Dev-Ref-No")}
        data = {"deactivated": "1", "csrf_token": self.csrf_token}
        r = self.patch(api_url, json=data, headers=headers)
        print('deactivate', r)
        data["deactivated"] = "0"
        r = self.patch(api_url, json=data, headers=headers)
        print('activate', r)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Keep WG-Gesucht.de ads on top of the listing by regularly toggling their activation status.')
    parser.add_argument("--interval", nargs=1, type=int, default=3600, help="How often to update the ads. Interval in seconds, default 3600 (1h).")
    parser.add_argument("ad_id", nargs="+", help="The IDs of the ads.")
    args = parser.parse_args()
    username = "ybsilas@gmail.com"
    password = getpass.getpass("password:")
    ad_id = args.ad_id[1]
    while True:
        session = WGGesuchtSession()
        session.login(username, password)
        session.toggle_activation(ad_id)
        time.sleep(args.interval[0])
