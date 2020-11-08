import mariadb
import dbcreds

def signUp(username, password):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO hackers (alias, password) VALUES (?,?)", [username, password])
        conn.commit()
        if cursor.rowcount == 1:
            print("A hacker is created!")
        else:
            print("Failed to create a hacker!")
    except mariadb.ProgrammingError:
        print("Beepoop. Program error...")
    except mariadb.DataError:
        print("Beepoop. Data error...")
    except mariadb.OperatianalError:
        print("Beepoop. Connection error...")
    finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()