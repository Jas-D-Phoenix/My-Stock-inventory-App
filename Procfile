web: cd stock_inventory && python manage.py migrate && gunicorn stock_inventory.wsgi:application --bind 0.0.0.0:$PORT
release: cd stock_inventory && python manage.py migrate
