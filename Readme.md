# WG Gesucht Updater
##  Usage
```bash
$ python -m venv venv
$ venv/bin/activate (something like that)
$ pip install -r requirements.txt
```
```bash
$ python wg-gesucht-updater.py -p ${password_env} -users [users] -ads [ad_ids] --wait 1000
```
You can use multiple users and ads and the requests will be sent in the
specified order separated by the specified wait time. By default the wait time
is between 700 and 1000 seconds

## Dockerfile
I've uploaded a docker file that with a few tweeks can be run using the free
tier on google compute engine or azure. You can also look at transforming the
script to be as an amazon lambda function.

