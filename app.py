import setup
import time
import os
import sys
import logging
from dB import cursor
import subprocess as sp

def logout():
    sp.call('clear',shell=True)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def main_menu_redirection(inp):
    if inp == 1:
        insertion()
    elif inp == 2:
        updation()
    elif inp == 3:
        deletion()
    elif inp == 4:
        generate_report()
    elif inp == 5:
        logout()
    else:
        sp.call('clear',shell=True)
        main_menu()

def main_menu():
    print('Welcome user!')
    print('======================= Main DB Menu =======================')
    print('1)--> Insertion')
    print('2)--> Updation')
    print('3)--> Deletion')
    print('4)--> Generate Report')
    print('5)--> Logout')
    print('------------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    main_menu_redirection(inp)

def main():
    setup.create_database()
    time.sleep(2)
    setup.create_tables()
    sp.call('clear',shell=True)
    setup.dump_data()
    time.sleep(1)
    main_menu()

if __name__ == '__main__':
    main()