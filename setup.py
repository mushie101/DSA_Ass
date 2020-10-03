import mysql.connector
from mysql.connector import errorcode
from dB import cursor

DB_NAME = 'ctf_competition'
TABLES = {}

TABLES['coder'] = (
    "CREATE TABLE `coder` ("
    "`Username` varchar(50) NOT NULL,"
    "`Team_ID` int NOT NULL,"
    "`First` varchar(15) NOT NULL,"
    "`Last` varchar(15) NOT NULL,"
    "`Captain_Username` varchar(50) NOT NULL,"
    "`Day` int(2) NOT NULL,"
    "`Month` int(2) NOT NULL,"
    "`Year` int(4) NOT NULL,"
    "`Age` int(2) NOT NULL,"
    "PRIMARY KEY (`Username`)"
    ") ENGINE=InnoDB"
)

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