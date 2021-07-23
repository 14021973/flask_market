import urllib

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"

params = urllib.parse.quote_plus('Driver={SQL Server};'
                      'Server=KZ-HP;'
                      'Database=test;'
                      'UID=kzaw;'
                       'PWD=123456;')
                      #'Trusted_Connection=yes;'
#
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='5aad6b3ffc03854668819530d6c679d6'
db = SQLAlchemy(app)

from market import  routs
