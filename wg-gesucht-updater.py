#!/usr/bin/env python3

import argparse
import time
import requests 
from bs4 import BeautifulSoup
import logging
from random import randrange

logging.basicConfig(level=logging.DEBUG)

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
        logging.debug('deactivate')
        print('deactivate', ad_id, r)
        data["deactivated"] = "0"
        r = self.patch(api_url, json=data, headers=headers)
        logging.debug("activate")
        print("activate", ad_id, r)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Keep WG-Gesucht.de ads on top of the listing by regularly toggling their activation status.')
    parser.add_argument("--ads", "-a", nargs="+", help="The IDs of the ads.")
    parser.add_argument("--users", "-u", nargs="+", help="The usernames of the ads.")
    parser.add_argument("-p", nargs="+", help="The passwords of the ads.")
    

    args = parser.parse_args()
    users, p, ad_ids = args.users, args.p, args.ads
    if len(users) == 1:
        users = [users[0]] * len(ad_ids)
    if len(p) == 1:
        p = [p[0]] * len(ad_ids)

    triplets = zip(users, p, ad_ids)

    while True:
        for u, p, ad_id in triplets:
            wait = randrange(500, 1000)
            session = WGGesuchtSession()
            session.login(u, p)
            session.toggle_activation(ad_id)
            logging.debug(wait)
            time.sleep(wait)


