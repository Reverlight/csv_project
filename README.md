# csv_project

Install:

1.Default set up:
``python manage.py makemigrations``
``python manage.py migrate``

2.Create file type.json with data:

``[{"model": "csv_app.type", "pk": 1, "fields": {"name": "Email"}}, {"model": "csv_app.type", "pk": 2, "fields": {"name": "Full name"}}, {"model": "csv_app.type", "pk": 3, "fields": {"name": "Job"}}, {"model": "csv_app.type", "pk": 4, "fields": {"name": "Date"}}, {"model": "csv_app.type", "pk": 5, "fields": {"name": "Phone"}}] ``

3.Add types

``python manage.py loaddata type.json``

4.Create admin user to log in
``python manage.py createsuperuser``

Video demo:
https://www.youtube.com/watch?v=BjL3AvEQWAI
