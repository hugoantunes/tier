import os

from app import settings
from flask import Flask

from app.views import hello_world


def create_app():

    app = Flask(__name__)
    app.config.from_object(settings)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # users routes
    app.add_url_rule('/', 'index', hello_world)

    return app
