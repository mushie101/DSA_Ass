import mysql.connector
from mysql.connector import errorcode
from dB import cursor

DB_NAME = 'ctf_competition'
TABLES = {}

TABLES['region'] = (
    "DROP TABLE IF EXISTS `REGION`,"
    "`RID` int(3) NOT NULL AUTO_INCREMENT,"
    "`Rname` varchar(50) NOT NULL,"
    "PRIMARY KEY (`RID`)"
    ") ENGINE=InnoDB"
)

TABLES['team'] = (
    
)

TABLES['']

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("connection to DB {} successful!".format(DB_NAME))

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("--> Creating table {} ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(" ; table {} exists".format(table_name))
            else:
                print(err.msg)