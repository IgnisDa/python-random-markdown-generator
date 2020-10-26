############################
Using mdgen in your projects
############################

Initially this project was conceived since I needed to populate my
`django <https://www.djangoproject.com/>`_ models with fake data. Here's
implementation using both django and
`flask <https://flask.palletsprojects.com/en/1.1.x/>`_.

Implementation in django
========================

We will create a `management command
<https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/>`_
which will let us create a model instance using :code:`python manage.py
createdata` and insert fake markdown data into it.

**my_app/models.py**

.. code-block:: python

    from django.db import models

    class MarkdownPost(models.Model):
        text = models.TextField()
        created_on = models.DateTimeField(auto_add_now=True)

**my_app/management/createdata.py**

.. code-block:: python

    from django.core.management.base import BaseCommand
    from my_app.models import MarkdownPost
    from mdgen import MarkdownPostProvider

    fake = Faker()
    fake.add_provider(MarkdownPostProvider)

    class Command(BaseCommand):
        def handle(self, *args, **options):
            MarkdownPost.objects.create(
                text = fake.post()
            )

You can then invoke this command using :code:`python manage.py
createdata`.

Implementation in flask
=======================

in app.py
    from flask import Flask
    from mdgen import MarkdownPostProvider
    from faker import Faker
    import markdown.extensions.fenced_code

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)

    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), nullable=False)
        body = db.Column(db.Text, nullable=False)
        pub_date = db.Column(db.DateTime, nullable=False,
            default=datetime.utcnow)
    @app.route('/')
    def index():
        fake = Faker()
        fake.add_provider(MarkdownPostProvider)
        text = fake.post()
        marked_down_text = markdown.markdown(text, extensions=["fenced_code"])
        p = Post(title=marked_down_text)
        return p

    if __name__ == '__main__':
        app.run()

