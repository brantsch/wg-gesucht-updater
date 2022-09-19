WG-Gesucht-Updater
==================
*English version below.*

Dieses Werkzeug dient dazu, Deine Anzeigen auf WG-Gesucht.de regelmäßig automatisiert zu bearbeiten,
damit sie oben in den Suchergebnissen stehen,
denn WG-Gesucht.de zeigt bevorzugt die neuesten Anzeigen zuoberst an.

Dazu deaktiviert dieses Skript die angegebenen Anzeigen und aktiviert sie sofort wieder.
Das genügt, damit sie wieder wie erst kürzlich eingestellt wirken.

Wie finde ich Anzeigennummern (ad_id)?
--------------------------------------

Öffne die Übersichtsseite Deiner Anzeigen („Meine Anzeigen“).
Dort wird Dir für jedes deiner Angebote die *Anzeigennummer* mit aufgelistet.

---

This tool serves to push your ads on WG-Gesucht.de to the top of the search results
by automatically editing them periodically,
because WG-Gesucht.de preferentially shows the newest ads on top of the list.

To achieve that, this script de-activates the given ads and immediately re-activates them.
That's enough to make them look as if recently posted.

How do I find Advertisement Numbers (ad_id)?
--------------------------------------------

Open the overview of your advertisements.
There you will be shown the *Anzeigennummer* for each of your ads.

Verwendung/Usage
----------------
```text
usage: wg-gesucht-updater.py [-h] [--wait INTERVAL] --ads [ad_id ...] -p
[PASSWORD] --users [ USERNAME ...]

arguments:
  -h, --help           Show this help message and exit
  -w, --wait INTERVAL  How often to update the ads. Interval in seconds,
                       default 1000. 
  -p                   Password
  -u, --users          Usernames
  --ads                ad_ids
```

Usage
-----
```bash
$ python -m venv venv
$ venv/bin/activate 
$ pip install -r requirements.txt
```
```bash
$ python wg-gesucht-updater.py -p ${password_env} -users [users] -ads [ad_ids] --wait 1000
```
You can use multiple users and ads and the requests will be sent in the
specified order separated by the specified wait time. By default the wait time
is between 700 and 1000 seconds

Dockerfile
----------
Make a few minor changes to the dockerfile in order to create an image and
thereafter a container.
