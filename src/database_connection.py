import sqlite3


def database_connection(databasename):
    db_connection = sqlite3.connect(f"data/{databasename}statistics.db")
    db_connection.isolation_level = None
    return db_connection
