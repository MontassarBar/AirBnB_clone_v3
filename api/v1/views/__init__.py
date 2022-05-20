#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import*


''' - import Blueprint from flask doc
    - create a variable app_views which is an instance of Blueprint
    - wildcard import of everything in the package api.v1.views.index '''


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
