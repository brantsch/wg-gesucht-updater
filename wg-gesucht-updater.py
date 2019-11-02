#!/usr/bin/env python3

import argparse
import getpass
import time

import requests
from bs4 import BeautifulSoup


class WGGesuchtSession(requests.Session):

    def login(self, user, password):
        """ Log in to wg-gesucht.de. Return a new session. """
        url = "https://www.wg-gesucht.de/ajax/api/Smp/api.php?action=login"
        data = {"login_email_username": user,
                "login_password": password,
                "login_form_autologin": "1",
                "display_language": "de"}
        self.get("https://www.wg-gesucht.de")
        self.post(url, json=data)
        response = self.get("https://www.wg-gesucht.de/meine-anzeigen.html")
        soup = BeautifulSoup(response.text)
        nodes = soup.select("input")
        self.csrf_token = nodes[0]["value"]
        nodes = soup.select("a.logout_button")
        self.user_id = nodes[0]["data-user_id"]

    def toggle_activation(self, ad_id):
        """ Deactivate and immediately re-activate the offer. """
        api_url = "https://www.wg-gesucht.de/api/offers/{}/users/{}".format(ad_id, self.user_id)
        headers = {"X-User-ID": self.user_id,
                   "X-Client-ID": "wg_desktop_website",
                   "X-Authorization": "Bearer " + self.cookies.get("X-Access-Token"),
                   "X-Dev-Ref-No": self.cookies.get("X-Dev-Ref-No")}
        data = {"deactivated": "1", "csrf_token": self.csrf_token}
        r = self.patch(api_url, json=data, headers=headers)
        data["deactivated"] = "0"
        r = self.patch(api_url, json=data, headers=headers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Keep WG-Gesucht.de ads on top of the listing by regularly toggling their activation status.')
    parser.add_argument("--interval", nargs=1, type=int, default=3600, help="How often to update the ads.")
    parser.add_argument("ad_id", nargs="+", help="The IDs of the ads.")
    args = parser.parse_args()
    username = input("username:")
    password = getpass.getpass("password:")
    while True:
        session = WGGesuchtSession()
        session.login(username, password)
        for ad_id in args.ad_id:
            session.toggle_activation(ad_id)
        time.sleep(args.interval)
