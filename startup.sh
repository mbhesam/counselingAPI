python /code/manage.py collectstatic --noinput
uwsgi --ini /code/moshavereAPI.uwsgi.ini
