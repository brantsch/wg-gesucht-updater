WG-Gesucht-Updater
==================
*English version below.*

Dieses Werkzeug dient dazu, Deine Anzeigen auf WG-Gesucht.de regelmäßig automatisiert zu bearbeiten,
damit sie oben in den Suchergebnissen stehen,
denn WG-Gesucht.de zeigt bevorzugt die neuesten Anzeigen zuoberst an.

Dazu deaktiviert dieses Skript die angegebenen Anzeigen und aktiviert sie sofort wieder.
Das genügt, damit sie wieder wie erst kürzlich eingestellt wirken.

---

This tool serves to push your ads on WG-Gesucht.de to the top of the search results
by automatically editing them periodically.

To achieve that, this script de-activates the given ads and immediately re-activates them.
That's enough to make them look as if recently posted.

Verwendung/Usage
----------------
```text
usage: wg-gesucht-updater.py [-h] [--interval INTERVAL] ad_id [ad_id ...]

positional arguments:
  ad_id                The IDs of the ads.

optional arguments:
  -h, --help           show this help message and exit
  --interval INTERVAL  How often to update the ads.

```