release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py import_data
web: daphne -b 0.0.0.0 -p $PORT marketplace.asgi:application
