import mysql.connector
import time
from mysql.connector import errorcode
from dB import cursor, db

DB_NAME = 'ctf_'
TABLES = {}

TABLES['region'] = (
    "CREATE TABLE `region` ("
    "`Region_ID` int(3) NOT NULL,"
    "`Rname` varchar(50) NOT NULL,"
    "UNIQUE (`RName`),"
    "PRIMARY KEY (`Region_ID`)"
    ") ENGINE=InnoDB"
)

TABLES['team'] = (
    "CREATE TABLE `team` ("
    "`Team_ID` int(3) NOT NULL,"
    "`TeamName` varchar(50) NOT NULL,"
    "`Coach` varchar(50),"
    "`Region_ID` int(3) NOT NULL,"
    "UNIQUE (`TeamName`),"
    "PRIMARY KEY (`Team_ID`),"
    "FOREIGN KEY (`Region_ID`) REFERENCES `region`(`Region_ID`) ON DELETE CASCADE"
    ")ENGINE=InnoDB"
)

TABLES['venue'] = (
    "CREATE TABLE `venue` ("
    "`Venue_ID` int(3) NOT NULL,"
    "`Venue` varchar(20) NOT NULL,"
    "UNIQUE (`Venue`),"
    "PRIMARY KEY (`Venue_ID`)"
    ")ENGINE=InnoDB"
)

TABLES['match'] = (
    "CREATE TABLE `match` ("
    "`TID1` int(3) NOT NULL,"
    "`TID2` int(3) NOT NULL,"
    "`WonBy` int(3),"
    "`MVP` int(3),"
    "`Day` int(2) NOT NULL,"
    "`Venue_ID` int(3) NOT NULL,"
    "PRIMARY KEY (`TID1`,`TID2`,`Day`),"
    "FOREIGN KEY (`TID1`) REFERENCES `team` (`Team_ID`) ON DELETE CASCADE,"
    "FOREIGN KEY (`TID2`) REFERENCES `team` (`Team_ID`) ON DELETE CASCADE,"
    "FOREIGN KEY (`Venue_ID`) REFERENCES `venue` (`Venue_ID`) ON DELETE CASCADE"
    ")ENGINE=InnoDB"
)

TABLES['player'] = (
    "CREATE TABLE `player` ("
    "`Player_ID` int(3) NOT NULL,"
    "`Username` varchar(20) NOT NULL,"
    "`Age` int(2) NOT NULL,"
    "`Team_ID` int(3) NOT NULL,"
    "PRIMARY KEY (`Player_ID`),"
    "FOREIGN KEY (`Team_ID`) REFERENCES `team` (`Team_ID`) ON DELETE CASCADE"
    ")ENGINE=InnoDB"
)

TABLES['player_type'] = (
    "CREATE TABLE `player_type`("
    "`Player_ID` int(3) NOT NULL,"
    "`Type` varchar(10) NOT NULL,"
    "PRIMARY KEY (`Player_ID`, `Type`),"
    "CHECK (Type = 'Attacker' OR Type = 'Defender'),"
    "FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`) ON DELETE CASCADE"
    ")ENGINE=InnoDB"
)

TABLES['battle'] = (
    "CREATE TABLE `battle` ("
    "`TID1` int(3) NOT NULL,"
    "`TID2` int(3) NOT NULL,"
    "`Team_ID` int(3) NOT NULL,"
    "`Venue_ID` int(3) NOT NULL,"
    "`Player_ID` int(3) NOT NULL,"
    "PRIMARY KEY (`TID1`, `TID2`, `Player_ID`),"
    "CHECK (Team_ID = TID1 OR Team_ID = TID2),"
    "FOREIGN KEY (`TID1`) REFERENCES `team` (`Team_ID`) ON DELETE CASCADE,"
    "FOREIGN KEY (`TID2`) REFERENCES `team` (`Team_ID`) ON DELETE CASCADE,"
    "FOREIGN KEY (`Team_ID`) REFERENCES `team` (`Team_ID`) ON DELETE CASCADE,"
    "FOREIGN KEY (`Venue_ID`) REFERENCES `venue` (`Venue_ID`) ON DELETE CASCADE,"
    "FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`) ON DELETE CASCADE"
    ")ENGINE=InnoDB"
)

TABLES['defender'] = (
    "CREATE TABLE `defender` ("
    "`Player_ID` int(3) NOT NULL,"
    "`Battles_Played` int(3) NOT NULL,"
    "`Points_Given` int(4) NOT NULL,"
    "`Traps_Triggered` int(4) NOT NULL,"
    "`Avg_Defence` float(6) NOT NULL,"
    "`Best_Ratio` varchar(15) NOT NULL,"
    "PRIMARY KEY (`Player_ID`),"
    "FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`) ON DELETE CASCADE,"
    "CHECK (Best_Ratio LIKE '[0-9]-[0-9][0-9]')"
    ")ENGINE=InnoDB"
)

TABLES['attacker'] = (
    "CREATE TABLE `attacker` ("
    "`Player_ID` int(3) NOT NULL,"
    "`Points` int(4) NOT NULL,"
    "`Battles_Played` int(3) NOT NULL,"
    "`Battles_No_Deaths` int(3) NOT NULL,"
    "`Avg_Attack` float(6) NOT NULL,"
    "`Highscore` int(15) NOT NULL,"
    "PRIMARY KEY (`Player_ID`),"
    "FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`) ON DELETE CASCADE,"
    "CHECK (Battles_No_Deaths <= Battles_Played)"
    ")ENGINE=InnoDB"
)

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("connection to DB {} successful!".format(DB_NAME))

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("--> Creating table {} ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(" ; table {} exists".format(table_name))
            else:
                print(err.msg)
        time.sleep(1)

def dump_data():
    cursor.execute("USE {}".format(DB_NAME))
    # ======================= Region Data Dump ======================= 
    try:
        sql = "INSERT INTO `region` (Region_ID, RName) VALUES (%s,%s)"
        val = [
            ( "1","South East Asia"),
            ("2","North America"),
            ("3","South America"),
            ("4","Australia"),
            ("5","Europe")
            ]
        cursor.executemany(sql,val)
        print('-->Region data has been dumped')
    except:
        print('-->Region dump data already exists!')
    # ======================= Team Data Dump ======================= 
    try:
        sql = "INSERT INTO `team` (Team_ID, TeamName, Coach, Region_ID) VALUES (%s,%s,%s,%s)"
        val = [
            ("110","Virtus Pro","Sream","1"),
            ("120","Cloud9","Shroud","2"),
            ("130","Australis","J0hn","3"),
            ("140","ENCE","DeviCe","4"),
            ("150","NaVi","kennyS","5")
        ]
        cursor.executemany(sql,val)
        print('-->Team data has been dumped!')
    except:
        print('-->Team dump data already exists!')
    # ======================= Venue Data Dump ======================= 
    try:
        sql = "INSERT INTO `venue` (Venue_ID, Venue) VALUES (%s,%s)"
        val = [
            ("68","Gachibowli Stadium"),
            ("69","Lords Stadium"),
            ("70","IEM Katowice"),
            ("20", "IEM Sydney"),
            ("21", "Buckingham Palace")
        ]
        cursor.executemany(sql,val)
        print('-->Venue data has been dumped!')
    except:
        print('-->Venue dump data already exists!')

    db.commit()