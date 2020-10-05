import setup
import time
from dB import cursor
import subprocess as sp

def main():
    setup.create_database()
    time.sleep(2)
    setup.create_tables()
    sp.call('clear',shell=True)
    setup.dump_data()

if __name__ == '__main__':
    main()