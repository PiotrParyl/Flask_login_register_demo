from flask import Flask, render_template
import mysql.connector
from .settings import Setings
import pandas as pd


db = mysql.connector.connect(
    host= Setings.host,
    user=Setings.user,
    passwd=Setings.passwd,
    database=Setings.database,
)
df = pd.read_sql_query("SELECT * FROM Users",db,index_col="email")
df2 = pd.read_sql_query("SELECT * FROM Users",db)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')


    return app



#=============================================== Funktions


def check_emial(email):
    x = df2['email'].tolist()

    return x


def check_pass(email):
    x = df.loc[f'{email}'].loc['password']

    return x