"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7rn3hp8u7g2efbca0-a.oregon-postgres.render.com",
        database="to_do_0sq3",
        user="to_do_0sq3_user",
        password="GdWF6fpySlfm04OwcOJRJGY3DgWvkrUj")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
