from flask import Flask, render_template
import mysql.connector

host="178.79.191.194"
user="maczo_all"
passwd="Pomidor123!@#"
database="webfiszki_db"

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')


    return app



#=============================================== Funktions


def email_check(db):
    pass
