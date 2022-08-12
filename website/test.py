import email
from re import X
import pandas as pd
import mysql.connector

class Setings():
    host="178.79.191.194"
    user="maczo_all"
    passwd="Pomidor123!@#"
    database="webfiszki_db"



db = mysql.connector.connect(
    host= Setings.host,
    user=Setings.user,
    passwd=Setings.passwd,
    database=Setings.database,
)

df = pd.read_sql_query("SELECT * FROM Users",db,index_col="email")
df2 = pd.read_sql_query("SELECT * FROM Users",db)


emaill = "marek@gmail.com"




def check_emial(email):
    x = df2['email'].tolist()

    return x


def check_pass(email):
    x = df.loc[f'{email}'].loc['password']

    return x

