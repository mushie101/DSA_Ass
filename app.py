import setup
import time
import os
import sys
from dB import cursor
import subprocess as sp

def generate_report(inp):
    cursor.execute("USE _ctf_c")
    if inp == 6:
        main_menu()
    
    elif inp == 1:
        print('======================= Report =======================',end="\n\n")
        print("Number of wins per team [wins, teamID]")
        sql = "SELECT COUNT(M.WonBy) \"COUNT\", T.Team_ID FROM `match` as M, `team` as T WHERE WonBy IS NOT NULL AND T.Team_ID = M.WonBy GROUP BY T.Team_ID"
        print("")
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
    
    elif inp==2:
        print('======================= Report =======================',end="\n\n")
        print('Best Attacker of the competition [Player ID, Username]')
        sql = "SELECT Player_ID, Username from player WHERE Player_ID = (SELECT Player_ID from attacker WHERE points = (SELECT MAX(Points) FROM attacker))"
        print("")
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
    
    elif inp==3:
        print('======================= Report =======================',end="\n\n") 
        print('Best Defender of the competition [Player ID, Username]')
        sql = "SELECT Player_ID, Username FROM player WHERE Player_ID = (SELECT Player_ID FROM defender WHERE Traps_Triggered = (SELECT MAX(Traps_Triggered) FROM defender))"  
        print("")
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)           

    elif inp==4:
        print('======================= Report =======================',end="\n\n") 
        print('Highest Individual Scorer of Competition [Player ID, Username]')
        sql = "SELECT Player_ID, Username FROM player WHERE Player_ID=(SELECT Player_ID FROM attacker WHERE Highscore = (SELECT MAX(Highscore) FROM attacker))"  
        print("")
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)           



def report_menu():
    sp.call('clear',shell=True)
    print('======================= Report Menu =======================')
    print('1)--> Number of wins for each team')
    print('2)--> Best attacker of the competition')
    print('3)--> Best defender of the competition')
    print('4)--> Highest individual score of an attacker')
    print('5)--> Number of players who are both attackers and defenders')
    print('6)--> Back to Main Menu')
    print('-----------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    generate_report(inp)

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