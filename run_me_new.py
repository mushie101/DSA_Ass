import setup
import time
import os
import sys
from dB import cursor, db
import subprocess as sp

def insertion(inp):
    if inp==8:
        main_menu()

    elif inp==1:
        print('======================= Insertion =======================',end="\n\n")
        print("Enter the new players details ->")
        new_player=[]
        new_player.append(int(input("Player ID > ")))
        new_player.append(input("Username > "))
        new_player.append(int(input("Age > ")))
        new_player.append(int(input("Team ID > ")))
        new_player.append(int(input("Captain ID > ")))
        print("")
        sql="INSERT INTO player VALUES('%d','%s','%d','%d','%d')" %(new_player[0],new_player[1],new_player[2],new_player[3],new_player[4])
        cursor.execute(sql)
        print('=======================***********=======================',end="\n\n")
        print("Select the type of player (1, 2 or 3) ->")
        print("1)--> Attacker")
        print("2)--> Defender")
        print("3)--> Both",end="\n\n")
        Type=int(input("Your Option > "))

        if Type==1:
            sql="INSERT INTO player_type VALUES (%d, 'Attacker')" %(new_player[0])
            cursor.execute(sql)

            sql="INSERT INTO attacker VALUES (%d,%d,%d,%d,%d,%d)" %(new_player[0],0,0,0,0,0)
            cursor.execute(sql)
            db.commit()     

            print('Updated Players Table -->',end="\n\n")
            sql="SELECT * FROM player"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")  

            print('Updated Attackers Table -->',end="\n\n")
            sql="SELECT * FROM attacker"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")       

        elif Type==2:
            sql="INSERT INTO player_type VALUES (%d, 'Defender')" %(new_player[0])
            cursor.execute(sql)

            sql="INSERT INTO defender VALUES (%d,%d,%d,%d,%d)" %(new_player[0],0,0,0,0)
            cursor.execute(sql)
            db.commit()     

            print('Updated Players Table -->',end="\n\n")
            sql="SELECT * FROM player"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")  

            print('Updated Defenders Table -->',end="\n\n")
            sql="SELECT * FROM defender"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")  
     
        elif Type==3:
            sql="INSERT INTO player_type VALUES (%d, 'Defender')" %(new_player[0])
            cursor.execute(sql)

            sql="INSERT INTO defender VALUES (%d,%d,%d,%d,%d)" %(new_player[0],0,0,0,0)
            cursor.execute(sql)

            sql="INSERT INTO player_type VALUES (%d, 'Attacker')" %(new_player[0])
            cursor.execute(sql)

            sql="INSERT INTO attacker VALUES (%d,%d,%d,%d,%d,%d)" %(new_player[0],0,0,0,0,0)
            cursor.execute(sql)
            db.commit() 

            print('Updated Players Table -->',end="\n\n")
            sql="SELECT * FROM player"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")

            print('Updated Attackers Table -->',end="\n\n")
            sql="SELECT * FROM attacker"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")

            print('Updated Defenders Table -->',end="\n\n")
            sql="SELECT * FROM defender"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result,end="\n\n")
        
        else:
            insertion(inp)
    
    elif inp==2:
        print('======================= Insertion =======================',end="\n\n")
        print("Enter the new Team's details ->")
        new_team=[]
        new_team.append(int(input("Team ID > ")))
        new_team.append(input("TeamName > "))
        new_team.append(input("Coach > "))
        new_team.append(int(input("Region_ID > ")))
        print("")

        sql="INSERT INTO team VALUES ('%d','%s','%s','%d')" %(new_team[0],new_team[1],new_team[2],new_team[3])
        cursor.execute(sql)
        db.commit()

        print('Updated Teams Table -->',end="\n\n")
        sql="SELECT * FROM team"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

    elif inp==3:
        print('======================= Insertion =======================',end="\n\n")
        Player_ID=int(input("Enter the Player ID of the Attacker who started Defending > "))
        
        sql="INSERT INTO player_type VALUES('%d', 'Defender')" %(Player_ID)
        cursor.execute(sql)

        sql="INSERT INTO defender VALUES (%d,%d,%d,%d,%d)" %(Player_ID,0,0,0,0)
        cursor.execute(sql)
        db.commit()

        print('Updated Players Table -->',end="\n\n")
        sql="SELECT * FROM player"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        print('Updated Player Type Table -->',end="\n\n")
        sql="SELECT * FROM player_type"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        print('Updated Defenders Table -->',end="\n\n")
        sql="SELECT * FROM defender"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

    elif inp==4:
        print('======================= Insertion =======================',end="\n\n")
        Player_ID=int(input("Enter the Player ID of the Defender who started Attacking > "))
        
        sql="INSERT INTO player_type VALUES('%d', 'Attacker')" %(Player_ID)
        cursor.execute(sql)

        sql="INSERT INTO attacker VALUES (%d,%d,%d,%d,%d,%d)" %(Player_ID,0,0,0,0,0)
        cursor.execute(sql)
        db.commit()

        print('Updated Players Table -->',end="\n\n")
        sql="SELECT * FROM player"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        print('Updated Player Type Table -->',end="\n\n")
        sql="SELECT * FROM player_type"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

        print('Updated Defenders Table -->',end="\n\n")
        sql="SELECT * FROM attacker"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

    elif inp==5:
        print('======================= Insertion =======================',end="\n\n")
        print("Enter the new Venue's details ->")
        Venue_ID=int(input("Venue ID > "))
        Venue_Name=input("Venue Name > ")
        sql="INSERT INTO venue VALUES('%d','%s')" %(Venue_ID, Venue_Name)
        cursor.execute(sql)
        db.commit()
        print('Updated Venues Table -->',end="\n\n")
        sql="SELECT * FROM venue"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

    elif inp==6:
        print('======================= Insertion =======================',end="\n\n")
        print("Enter the details for the match for which the MVP is to be inserted ->")
        Tid1=int(input("TeamID 1 > "))
        Tid2=int(input("TeamID 2 > "))
        Day=int(input("Day > "))
        Mvp=int(input("Most Valuable Player > "))
        sql="UPDATE `match` SET MVP='%d' WHERE ((TID1='%d' AND TID2='%d' AND Day='%d') OR (TID2='%d' AND TID1='%d' AND Day='%d'))"%(Mvp,Tid1,Tid2,Day,Tid1,Tid2,Day)
        cursor.execute(sql)
        db.commit()
        print('Updated Matches Table -->',end="\n\n")
        sql="SELECT * FROM `match`"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")

    elif inp==7:
        print('======================= Insertion =======================',end="\n\n")
        print("Enter the details for the match for which Won By is to be inserted ->")
        Tid1=int(input("TeamID 1 > "))
        Tid2=int(input("TeamID 2 > "))
        Day=int(input("Day > "))
        WonBy=int(input("Team ID of the winner > "))     
        sql="UPDATE `match` SET WonBy='%d' WHERE ((TID1='%d' AND TID2='%d' AND Day='%d') OR (TID2='%d' AND TID1='%d' AND Day='%d'))"%(WonBy,Tid1,Tid2,Day,Tid1,Tid2,Day)
        cursor.execute(sql)
        db.commit()
        print('Updated Matches Table -->',end="\n\n")
        sql="SELECT * FROM `match`"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result,end="\n\n")   

    else:
        insertion_menu()

    inp = input("Enter any key to go back to the main menu> ")
    main_menu() 
    

def insertion_menu():
    cursor.execute("USE _ctf_c_t")
    sp.call('clear',shell=True)
    print('======================= Insertion Menu =======================')
    print('1)--> Insertion of a New Player into a Team')
    print('2)--> Insertion of a New Team into the Competition')
    print('3)--> Insertion of a New Defender record if an Attacker starts Defending')
    print('4)--> Insertion of  a New Attacker record if a Defender starts Attacking')
    print('5)--> Insertion of a New Venue if a new stadium is constructed')
    print('6)--> Inserting the MVP entry after a match is over')
    print('7)--> Inserting the Won By entry after the match is over')
    print('8)--> Back to Main menu')
    print('--------------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    insertion(inp)

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

    else:
        updation_menu()

    inp = input("Enter any key to go back to the main menu> ")
    main_menu() 
    


def updation_menu():
    cursor.execute("USE _ctf_c_t")
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
    cursor.execute("USE _ctf_c_t")
    sp.call('clear',shell=True)
    print('======================= Deletion Menu =======================')
    print('1)--> Demolition of a Venue')
    print('2)--> Back to main menu')
    print('-------------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    deletion(inp)


def generate_report(inp):
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

def show_table():
    cursor.execute("USE _ctf_c_t")
    sp.call('clear',shell=True)
    print('======================= Select Table =======================')
    print('1)--> Region')
    print('2)--> Team')
    print('3)--> Venue')
    print('4)--> Player')
    print('5)--> Player Type')
    print('6)--> Battle')
    print('7)--> Attacker')
    print('8)--> Defender')
    print('9)--> Back to Main Menu')
    print('-----------------------------------------------------------')
    inp = int(input("Enter Option:- "))
    print_table(inp)
    
def print_table(inp):
    if inp == 9:
        main_menu()
    elif inp == 1:
        print('======================= Region =======================',end="\n\n")
        sql = "select * from `region`"
        print("")
    
    elif inp==2:
        print('======================= Team =======================',end="\n\n")
        sql = "select * from `team`"
        print("")
    
    elif inp==3:
        print('======================= Venue =======================',end="\n\n") 
        sql = "select * from `venue`"
        print("")         

    elif inp==4:
        print('======================= Player =======================',end="\n\n") 
        sql = "select * from `player`"
        print("")     

    elif inp==5:
        print('======================= Player Type =======================',end="\n\n") 
        sql = "select * from `player_type`"
        print("")


    elif inp==6:
        print('======================= Battle =======================',end="\n\n") 
        sql = "select * from `battle`"
        print("")


    elif inp==7:
        print('======================= Attacker =======================',end="\n\n") 
        sql = "select * from `attacker`"
        print("")


    elif inp==8:
        print('======================= Defender =======================',end="\n\n") 
        sql = "select * `defender`"
        print("")


    else:
        report_menu()  
    
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    inp = input("Enter any key to go back to the main menu> ")
    main_menu()
    
    
    
def report_menu():
    cursor.execute("USE _ctf_c_t")
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
        show_table()
    elif inp == 6:
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
    print('5)--> Show Table')
    print('6)--> Logout')
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
