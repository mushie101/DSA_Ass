import setup
from dB import cursor
import subprocess as sp

def main():
    setup.create_database()
    setup.create_tables()

if __name__ == '__main__':
    main()