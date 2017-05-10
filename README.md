## Patients service

  0. Requirements:
    * OS: Ubuntu 14.04
    * Packages:
        * postgresql-9.4
        * python3.4
        * python3.4-dev
        * python3-pip
        * virtualenvwrapper
        * git
        * nginx
        * supervisor
        * libpq-dev
        * uwsgi
        * uwsgi-plugin-python3
        * rabbitmq-server

    * Install dependencies for lxml
    * sudo apt-get install libxml2-dev libxslt1-dev python-dev

    * Install dependencies for Pillow
    * sudo apt-get install libjpeg-dev

    * Install wkhtmltopdf
    * sudo add-apt-repository ppa:ecometrica/servers
    * sudo apt-get update
    * sudo apt-get install wkhtmltopdf

1. Clone repo
    * sudo mkdir /srv/www/ -p
    * sudo mkdir /srv/www/IgoStories -p
    * sudo chown -R user:group /srv/www/IgoStories
    * sudo chmod 755 /srv/www/IgoStories
    * cd /srv/www/IgoStories && git clone https://github.com/Denvert/Igostories-Admin-API.git .
    * git chechout develop

2. Create virtualenv for python3
    * sudo mkdir -p /srv/www/venv
    * sudo chown -R user:group /srv/www/venv
    * sudo chmod -R 644 /srv/www/venv
    * cd /srv/www/venv && virtualenv -p /usr/bin/python3 igostories_env
    * . /srv/www/venv/igostories_env/bin/activate
    * pip install -r /srv/www/IgoStories/requirements.txt

3. Create database
    * sudo -u postgres psql -f /srv/www/IgoStories/tools/create_db.sql
    * cp /srv/www/IgoStories/igostories/settings/local.sample.py /srv/www/IgoStories/igostories/settings/local.py
    * change user name and password in local settings - nano /srv/www/IgoStories/igostories/settings/local.py
    * cd /srv/www/IgoStories && python manage.py migrate

4. Collect static
    * cd /srv/www/IgoStories && python manage.py collectstatic --noinput

5. Copy configs for nginx, supervisor and uwsgi
    * sudo ln -sf /srv/www/IgoStories/tools/server-configs/nginx/igostories.conf /etc/nginx/conf.d/
    * sudo ln -sf /srv/www/IgoStories/tools/server-configs/supervisor/igostories-supervisor.conf /etc/supervisor/conf.d/
    * sudo ln -sf /srv/www/IgoStories/tools/server-configs/uwsgi/uwsgi.ini /etc/uwsgi/
    * sudo ln -sf /srv/www/IgoStories/tools/server-configs/uwsgi/uwsgi.conf /etc/init/

6. Restart services:
    * sudo service nginx restart
    * sudo service uwsgi restart