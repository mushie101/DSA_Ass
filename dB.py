import mysql.connector

config={
    'user':'root',
    'password': '23314247H@me',
    'auth_plugin':'mysql_native_password'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()