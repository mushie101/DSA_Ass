import mysql.connector
import getpass

Username=input("Username: ")
Password=getpass.getpass()

config={
    'user':Username,
    'password': Password,
    'auth_plugin':'mysql_native_password'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
