from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from db import init_db

init_db()

from api import views, model