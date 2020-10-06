import setup
import time
import os
import sys
import logging
from dB import cursor
import subprocess as sp

def report_menu():
    sp.call('clear',shell=True)
    print('======================= Report Menu =======================')
    print('1)--> Number of wins for each team')
    print('2)--> Best attacker of the tournament')
    print('3)--> Best defender of the tournament')
    print('4)--> Highest individual score of an attacker')
    print('5)--> Number of players who are both attackers and defenders')
    print('6)--> Back to Main Menu')
    print('-----------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    #generate_report(inp)

def logout():
    sp.call('clear',shell=True)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def main_menu_redirection(inp):
    if inp == 1:
        insertion_menu()
    elif inp == 2:
        updation_menu()
    elif inp == 3:
        deletion_menu()
    elif inp == 4:
        report_menu()
    elif inp == 5:
        logout()
    else:
        sp.call('clear',shell=True)
        main_menu()

def main_menu():
    sp.call('clear',shell=True)
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