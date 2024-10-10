import sqlite3


def connect():
    connection = sqlite3.connect("user.db")
    return connection


def existing_table():
    sqldb = """CREATE TABLE IF NOT EXISTS users (
    user_id TEXT NOT NULL,
    user_name TEXT NOT NULL,
    user_password TEXT NOT NULL,
    CONSTRAINT pk_user_id PRIMARY KEY (user_id)
    );"""

    condb = connect()
    curdb = condb.cursor()
    curdb.execute(sqldb)
    condb.commit()
    condb.close()


def retrieve_info(dataType):
    if dataType == "s":
        sqldb = "SELECT user_id, user_name FROM users ORDER BY user_id"
    else:
        sqldb = "SELECT * FROM users ORDER BY user_id"

    condb = connect()
    curdb = condb.cursor()
    datdb = curdb.execute(sqldb).fetchall()
    condb.close()
    return datdb
