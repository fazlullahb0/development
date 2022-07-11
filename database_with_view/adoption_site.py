#adoption_site.py
import os
# from forms import AddForm, DelForm
from flask import Flask,render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'myapp'

if __name__ == '__main__':
    app.run(debug=True)
