import urllib.parse
from uuid import uuid5, NAMESPACE_URL

from flask import request, json
from flask.views import MethodView

from app.db import db


def hello_world():
    return "hallo"


class UrlHandler(MethodView):

    header = {'Content-Type': 'application/json; charset=UTF-8'}

    def post(self):
        data_dict = json.loads(request.data)
        url_original = data_dict['url']

        parsed_url = urllib.parse.quote_plus(url_original)
        url_short = db.get(parsed_url)
        if not url_short:
            url_short = str(uuid5(NAMESPACE_URL, url_original))
            db.set(f'{parsed_url}', url_short)
            db.set(f'{url_short}:original', url_original)
            db.set(f'{url_short}:counter', 0)
        response = {
            'original': url_original,
            'short': str(url_short)
        }

        return(response, 200)
