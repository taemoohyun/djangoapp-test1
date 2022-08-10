release: python manage.py migrate
web: gunicorn djangoapp_test1.wsgi --log-file=-
web: heroku config:set DEBUG_COLLECTSTATIC=1