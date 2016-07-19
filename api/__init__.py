from flask import Flask
from flask.ext.cache import Cache


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# Check Configuring Flask-Cache section for more details
cache = Cache(app,config={'CACHE_TYPE': 'memcached'})

from db import init_db

init_db()

from api import views, model