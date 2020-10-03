import mysql.connector
from dB import cursor

DB_NAME = 'ctf_competition'

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("database {} succesfully created".format(DB_NAME))

create_database()