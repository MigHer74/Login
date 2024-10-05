import sqlite3


def connect():
    connection = sqlite3.connect("user.db")
    return connection


def existing_table():
    sqldb = """CREATE TABLE IF NOT EXISTS users (
    user_id TEXT NOT NULL,
    user_name TEXT,
    user_password TEXT,
    CONSTRAINT pk_user_id PRIMARY KEY (user_id)
    );"""

    condb = connect()
    curdb = condb.cursor()
    curdb.execute(sqldb)
    condb.commit()
    condb.close()


def retrieve_info():
    condb = connect()
    curdb = condb.cursor()
    datdb = curdb.execute("SELECT * FROM users ORDER BY user_id").fetchall()
    condb.close()
    return datdb

