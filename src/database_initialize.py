from database_connection import database_connection


def initialize_database(databasename):
    db_connection = database_connection(databasename)

    table = db_connection.execute(
        '''SELECT name FROM sqlite_master WHERE type='table' AND name=?;''',
        ["Results"]).fetchall()
    print(f"tabel:{table}")
    if table == []:
        create_tables(db_connection)

    return db_connection


def create_tables(db_connection):
    db_connection.execute(
        "CREATE TABLE Results(id INTEGER PRIMARY KEY, level INTERGER, score FLOAT)")


# if __name__ == "__main__":
#     initialize_database()
