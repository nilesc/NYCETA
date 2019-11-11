import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print(error)
    return conn


def get_db_description(conn):
    """Obtain the description of tables
    and columns in the database

    :conn: connection object to the database
	"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
