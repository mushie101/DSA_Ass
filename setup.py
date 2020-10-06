import mysql.connector
import time
from mysql.connector import errorcode
from dB import cursor, db

DB_NAME = '_ctf_c_t'
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
    "`Captain_ID` int(3) NOT NULL,"
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
    "PRIMARY KEY (`Player_ID`),"
    "FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`) ON DELETE CASCADE"
    ")ENGINE=InnoDB"
)

TABLES['attacker'] = (
    "CREATE TABLE `attacker` ("
    "`Player_ID` int(3) NOT NULL,"
    "`Points` int(5) NOT NULL,"
    "`Battles_Played` int(3) NOT NULL,"
    "`Battles_No_Deaths` int(3) NOT NULL,"
    "`Avg_Attack` float(6) NOT NULL,"
    "`Highscore` int(15) NOT NULL,"
    "PRIMARY KEY (`Player_ID`),"
    "FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`) ON DELETE CASCADE"
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
    # ======================= Match Data Dump =======================
    try:
        sql = "INSERT INTO `match` (TID1, TID2, WonBy, MVP, Day, Venue_ID) VALUES (%s,%s,%s,%s,%s,%s)"
        val = [
            ("110","120","110","111","1","68"),
            ("130","150","150","152","2","70"),
            ("120","140","120","121","2","69"),
            ("110","130","110","112","3","68"),
            ("140","150","140","141","3","21"),
            ("140","130","130","131","4","20"),
            ("150","120", None, None,"4","69"),
            ("140","150", None, None,"5","69"),
            ("130","110", None, None,"6","68")
        ]
        cursor.executemany(sql,val)
        print('-->Match data has been dumped!')
    except:
        print('-->Match dump data already exists!')
    # ======================= Player Data Dump =======================
    try:
        sql = "INSERT INTO `player` (PLayer_ID, Username, Age, Team_ID, Captain_ID) VALUES (%s,%s,%s,%s,%s)"
        val = [
            ("111","Mu5H1E","21","110","111"),
            ("112","Critikal","19","110","111"),
            ("113","Champ12134","24","110","111"),
            ("114","Negative","16","110","111"),
            ("121","Peter","30","120","121"),
            ("122","HarryPotter","20","120","121"),
            ("131","Vijay","21","130","131"),
            ("132","Siddarth","20","130","131"),
            ("141","Saud","29","140","142"),
            ("142","Sharaf","27","140","142"),
            ("151","Zakariya","21","150","151"),
            ("152","Razzak","20","150","151")
        ]
        cursor.executemany(sql,val)
        print('-->Player data has been dumped!')
    except:
        print('-->Player dump data already exists!')
    # ======================= Player Type Data Dump =======================
    try:
        sql = "INSERT INTO `player_type` (Player_ID,Type) VALUES (%s,%s)"
        val = [
            ("111","Attacker"),
            ("111","Defender"),
            ("112","Attacker"),
            ("112","Defender"),
            ("113","Attacker"),
            ("114","Attacker"),
            ("121","Attacker"),
            ("122","Attacker"),
            ("122","Defender"),
            ("131","Attacker"),
            ("131","Defender"),
            ("132","Defender"),
            ("141","Attacker"),
            ("141","Defender"),
            ("142","Attacker")
        ]
        cursor.executemany(sql,val)
        print('-->Player type data has been dumped!')
    except:
        print('-->Player type dump data already exists!')
    # ======================= Battle Data Dump =======================
    try:
        sql = "INSERT INTO `battle` (TID1,TID2,Team_ID,Venue_ID,PLayer_ID) VALUES (%s,%s,%s,%s,%s)"
        val = [
            ("110", "120", "110", "68", "111"),
            ("110", "120", "110", "68", "112"),
            ("110", "120", "110", "68", "113"),
            ("110", "120", "110", "68", "114"),
            ("110", "120", "120", "68", "121"),
            ("110", "120", "120", "68", "122"),
            ("130", "150", "130", "69", "131"),
            ("130", "150", "130", "69", "132"),
            ("130", "150", "150", "69", "151"),
            ("130", "150", "150", "69", "152")
        ]
        cursor.executemany(sql,val)
        print('-->Battle data has been dumped!')
    except:
        print('-->Battle dump data already exists!')
    # ======================= Defender Data Dump =======================
    try:
        sql = "INSERT INTO `defender` (Player_ID,Battles_Played,Points_Given,Traps_Triggered,Avg_Defence) VALUES (%s,%s,%s,%s,%s)"
        val = [
            ("111", "404", "1324", "342", "4"),
            ("112", "4", "25", "12", "2"),
            ("122", "234", "2353", "12", "196"),
            ("131", "87", "456", "10", "46"),
            ("132", "123", "2082", "243", "8"),
            ("141", "27", "1324", "45", "29")
        ]
        cursor.executemany(sql,val)
        print('-->Defender data has been dumped!')
    except:
        print('-->Defender dump data already exists!')
    # ======================= Attacker Data Dump =======================
    try:
        sql = "INSERT INTO `attacker` (Player_ID,Points,Battles_Played,Battles_No_Deaths,Avg_Attack,Highscore) VALUES (%s,%s,%s,%s,%s,%s)"
        val = [
            ("111", "18456", "404", "48", "52", "200"),
            ("112", "4", "3", "478", "478", "254"),
            ("113", "11578", "240", "20", "53", "183"),
            ("114", "8467", "125", "11", "74", "264"),
            ("121","6456","304","25","23","156"),
            ("122","3457","234","8","15","99"),
            ("131","2076","87","6","26","124"),
            ("141","786","27","1","30","67"),
            ("142","1256","54","6","26","163")
        ]
        cursor.executemany(sql,val)
        print('-->Attacker data has been dumped!')
    except:
        print('-->Attacker dump data already exists!')
        
    db.commit()