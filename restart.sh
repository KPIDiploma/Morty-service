#!/usr/bin/env bash

sudo kill -9 $(pgrep -f uwsgi)
sudo uwsgi --ini=/etc/uwsgi/uwsgi.ini#!/usr/bin/env bash