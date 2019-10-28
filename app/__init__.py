import os

from app import settings
from flask import Flask

from app.views import hello_world, UrlHandler, RedirectHandler


def create_app():

    app = Flask(__name__)
    app.config.from_object(settings)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # users routes
    app.add_url_rule('/', 'index', hello_world)

    url_view = UrlHandler.as_view('url_api')
    app.add_url_rule(
        '/url',
        view_func=url_view,
        methods=['POST']
    )

    url_view = RedirectHandler.as_view('redirect_api')
    app.add_url_rule(
        '/<string:url_short>',
        view_func=url_view,
        methods=['GET']
    )
    return app
