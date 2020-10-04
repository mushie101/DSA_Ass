import setup
import pymysql 

def main():
    setup.create_database()
    setup.create_tables()

if __name__ == '__main__':
    main()