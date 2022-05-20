#!/usr/bin/python3
import os
from models import storage
from flask import Flask
from api.v1.views import app_views


'''f'''
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def S_C(err):
    '''close storage'''
    storage.close()


if __name__ == "__main__":
    '''run Flask server'''
    host = os.environ.get('HBNB_API_HOST')
    port = os.environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
