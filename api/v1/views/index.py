#!/usr/bin/python3
import json
from api.v1.views import app_views

''' - import app_views from api.v1.views
    - create a route /status on the object app_views that
        returns a JSON: "status": "OK" '''


@app_views.route('/status', strict_slashes=False)
def status():
    return json.loads('{"status": "OK"}')
