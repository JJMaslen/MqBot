import sqlite3
from sqlite3 import Error

# Base Commands
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_entry(conn, entry, sql):
    cur = conn.cursor()
    cur.execute(sql, entry)
    conn.commit()

def read_table(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    return rows

def table_names(conn, sql):
    cur = conn.cursor()
    return cur.execute(sql)

# Custom Commands
def createTable_EventTable(host):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql_create_raidEvents_table = """ CREATE TABLE IF NOT EXISTS raidEvents{}  (
                                        name text PRIMARY KEY, 
                                        role text NOT NULL,
                                        time text,
                                        wings text
                                        
                                        ); """.format(host)
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_raidEvents_table)
    else:
        print("Error! Cannot create the database connection")

def readTable(host):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql = '''SELECT '''

def checkTable(host):
    file = open("databasePath.txt", "r")
    database = file.read()
    file.close()
    sql = '''SELECT name FROM sqlite_master WHERE type = 'table'; '''

    conn = create_connection(database)
    tableTitles = table_names(conn, sql)

    # find if the host already has a table
    for name in tableTitles:
        if host in name[0]:
            return True

    return False

def addPlayer(host, user, role, time, wings):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql = """ INSERT INTO raidEvents{}(name, role, time, wings) VALUES(?,?,?,?)""".format(host)
    conn = create_connection(database)
    with conn:
        NewEntry = (user, role, time, wings)
        add_entry(conn, NewEntry, sql)