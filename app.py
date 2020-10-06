import setup
import time
import os
import sys
from dB import cursor, db
import subprocess as sp

def updation(inp):
    if inp==5:
        main_menu()

    elif inp==1:
        print('======================= Updation =======================',end="\n\n")
        print("Attacker Table -> ",end="\n\n")
        sql = "SELECT * FROM attacker;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")
        Player_ID=int(input("Enter the ID of the attacker who's data needs to be updated > "))
        sql = "SELECT * FROM attacker WHERE (Player_ID = %d)" %(Player_ID)
        cursor.execute(sql)
        result=cursor.fetchall()
        points_gained=int(input("Enter the number of points gained by the attacker > "))
        Trap_Triggered=int(input("Enter 0 if the attacker did not trigger any traps > "))
        
        if Trap_Triggered:
            Battle_No_Deaths=0
        else:
            Battle_No_Deaths=1
        
        sql = "UPDATE attacker SET Battles_Played = %d WHERE Player_ID = %d" %(int(int(result[0][2])+1),Player_ID)
        cursor.execute(sql)
        db.commit()

        sql = "UPDATE attacker SET Points = '%d' WHERE Player_ID = '%d'" %(result[0][1]+points_gained , Player_ID)
        cursor.execute(sql)
        db.commit()

        sql = "UPDATE attacker SET Battles_No_Deaths = %d WHERE Player_ID = %d" %(result[0][3]+Battle_No_Deaths, Player_ID)
        cursor.execute(sql)
        db.commit()

        sql = "UPDATE attacker SET Avg_Attack = '%f' WHERE Player_ID = '%d'" %(float(float(result[0][1])/float(result[0][2]-result[0][3])) , Player_ID)
        cursor.execute(sql)
        db.commit()

        if result[0][5] < points_gained:
            sql = "UPDATE attacker SET Highscore = '%d' WHERE Player_ID = '%d'" %(points_gained, Player_ID)
            cursor.execute(sql)
            db.commit() 

        print('Updated Table -->',end="\n\n")
        sql="SELECT * FROM attacker"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)

    elif inp==2:
        print('======================= Updation =======================',end="\n\n")
        print("Defender Table -> ",end="\n\n")
        sql = "SELECT * FROM defender;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")
        Player_ID=int(input("Enter the ID of the defender who's data needs to be updated > "))
        sql = "SELECT * FROM defender WHERE (Player_ID = %d)" %(Player_ID)
        cursor.execute(sql)
        result=cursor.fetchall()
        points_given=int(input("Enter the number of points given by the defender > "))
        Trap_Laid=int(input("Number of successful traps laid by the defender > "))
        
        sql = "UPDATE defender SET Battles_played = '%d' WHERE Player_ID = '%d'" %(result[0][1]+1, Player_ID)
        cursor.execute(sql)
        db.commit()
 
        sql = "UPDATE defender SET Points_Given = '%d' WHERE Player_ID = '%d'" %(result[0][2]+points_given , Player_ID)
        cursor.execute(sql)
        db.commit()       

        sql = "UPDATE defender SET Traps_Triggered = '%d' WHERE Player_ID = '%d'" %(result[0][3]+Trap_Laid , Player_ID)
        cursor.execute(sql)
        db.commit()

        sql = "UPDATE defender SET Avg_Defence = '%f' WHERE Player_ID = '%d'" %(float(float(result[0][2])/float(result[0][1])) , Player_ID)
        cursor.execute(sql)
        db.commit() 

        print('Updated Table -->',end="\n\n")
        sql="SELECT * FROM defender"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)      

    elif inp==3:
        print('======================= Updation =======================',end="\n\n")
        print("Venue Table -> ",end="\n\n")
        sql = "SELECT * FROM venue;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        print("Matches Table -> ",end="\n\n")
        sql = "SELECT * FROM `match`;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        Tid1 = int(input("Enter the first team's ID > "))
        Tid2 = int(input("Enter the second teams ID > "))
        Day = int(input("Enter the day of the Match > "))
        Venue_ID = int(input("Enter the Venue ID where match is to be held instead > "))
        
        sql = "UPDATE `match` SET Venue_ID = '%d' WHERE Day = '%d' AND TID1 = '%d' AND TID2 = '%d'" %(Venue_ID, Day, Tid1, Tid2)
        cursor.execute(sql)
        db.commit()
        
        print("Updated Matches Table -> ",end="\n\n")
        sql = "SELECT * FROM `match`;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")       

    elif inp==4:
        print('======================= Updation =======================',end="\n\n")
        print("Players Table -> ",end="\n\n")
        sql = "SELECT * FROM player;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        Player_ID=int(input("Enter the ID of the player who has been deceased > "))

        sql = "UPDATE player SET Age = '%d' WHERE Player_ID = '%d'" %(-1, Player_ID)
        cursor.execute(sql)
        db.commit()

        print("Updated players Table -> ",end="\n\n")
        sql = "SELECT * FROM player;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

def updation_menu():
    cursor.execute("USE _ctf_c")
    sp.call('clear',shell=True)
    print('======================= Updation Menu =======================')
    print('1)--> Updating records of attacker after every match')
    print('2)--> Updating records of defender after every match')
    print('3)--> Updating venue if there is relocation')
    print('4)--> Updating age of player to -1 if he dies')
    print('5)--> Back to Main Menu')
    print('-------------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    updation(inp)


def deletion(inp):
    if inp==1:
        print('======================= Deletion =======================',end="\n\n")
        sql = "SELECT * FROM venue;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print("The venue list -->",end="\n\n")
        print(result,end="\n\n")
        
        sql = "SELECT * FROM `match`;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print("The match list -->",end="\n\n")
        print(result,end="\n\n")
        
        Venue_ID_Demolish=int(input("enter the venue ID you want to delete > "))
        Venue_ID_Replace=int(input("enter the venue ID of the replacement for the match > "))
        sql = "UPDATE `match` SET Venue_ID = '%d' WHERE Venue_ID = '%d'" %(Venue_ID_Replace, Venue_ID_Demolish)       
        cursor.execute(sql)
        db.commit()
        sql = "DELETE FROM venue WHERE (Venue_ID = '%d')" %(Venue_ID_Demolish)
        cursor.execute(sql)
        db.commit()
        print('--> The venue has been succesfully deleted!')
    
    elif inp==2:
        main_menu()

    else:
        deletion_menu()

    inp = input("Enter any key to go back to the main menu> ")
    main_menu() 

def deletion_menu():
    cursor.execute("USE _ctf_c")
    sp.call('clear',shell=True)
    print('======================= Deletion Menu =======================')
    print('1)--> Demolition of a Venue')
    print('2)--> Back to main menu')
    print('-------------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    deletion(inp)


def generate_report(inp):
    cursor.execute("USE _ctf_c")
    if inp == 6:
        main_menu()
    
    elif inp == 1:
        print('======================= Report =======================',end="\n\n")
        print("Number of wins per team [wins, teamID]")
        sql = "SELECT COUNT(M.WonBy) \"COUNT\", T.Team_ID FROM `match` as M, `team` as T WHERE WonBy IS NOT NULL AND T.Team_ID = M.WonBy GROUP BY T.Team_ID"
        print("")
    
    elif inp==2:
        print('======================= Report =======================',end="\n\n")
        print('Best Attacker of the competition [Player ID, Username]')
        sql = "SELECT Player_ID, Username from player WHERE Player_ID = (SELECT Player_ID from attacker WHERE points = (SELECT MAX(Points) FROM attacker))"
        print("")
    
    elif inp==3:
        print('======================= Report =======================',end="\n\n") 
        print('Best Defender of the competition [Player ID, Username]')
        sql = "SELECT Player_ID, Username FROM player WHERE Player_ID = (SELECT Player_ID FROM defender WHERE Traps_Triggered = (SELECT MAX(Traps_Triggered) FROM defender))"  
        print("")         

    elif inp==4:
        print('======================= Report =======================',end="\n\n") 
        print('Highest Individual Scorer of Competition [Player ID, Username]')
        sql = "SELECT Player_ID, Username FROM player WHERE Player_ID=(SELECT Player_ID FROM attacker WHERE Highscore = (SELECT MAX(Highscore) FROM attacker))"  
        print("")     

    elif inp==5:
        print('======================= Report =======================',end="\n\n") 
        print('Number of all rounders in the competition (both attackers and defenders)')
        sql = "SELECT COUNT(*) FROM (SELECT PLayer_ID, COUNT(Player_ID) FROM player_type GROUP BY Player_ID HAVING COUNT(Player_ID)=2) A"  
        print("")

    else:
        report_menu()  
    
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    inp = input("Enter any key to go back to the main menu> ")
    main_menu() 



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