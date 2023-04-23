import sqlite3


def database_connection():
    db_connection = sqlite3.connect("data/gamestatitics.db")
    db_connection.isolation_level = None
    return db_connection
