# django_app_v3.2 - About candidate

This project is based on Django 3.2.

- "Writing your first Django app" with Django 3.2 (polls application).
- An app called "about", who is a platform for candidates to get a job.

NOTES:

- To probe this project, you should istalled django 3.2 and pillow (you can install a virtualenv and install this apps with pip). 

- By default, the database used in this project is PostgreSQL. Otherwise, you can change the `settings.py` file and replace the `DATABASES` constant with:

  `DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }`
  
- Then, migrate and thats it.
- If you want to load a few examples in your DB, you should use the file "db.json".
  - Use the command `python manage.py loaddata db.json`

Preview

Home (Redirects to about): https://jeluengasm.pythonanywhere.com/

About app: https://jeluengasm.pythonanywhere.com/about

Polls app: https://jeluengasm.pythonanywhere.com/polls

Django admin for polls and about apps: https://jeluengasm.pythonanywhere.com/admin/

    user: guest
    pass: 123456789
