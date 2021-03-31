import sqlite3

#CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT, analysis real)"
CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS entries
                    (content TEXT, date TEXT, analysis TEXT)'''


CREATE_ENTRY = "INSERT INTO entries VALUES (?, ?, ?)"
RETRIEVE_ENTRIES = "SELECT * FROM entries"


def create_tables():
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_TABLE)


def create_entry(content, date, analysis):
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_ENTRY, (content, date, analysis))


def retrieve_entries():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES)
        return cursor.fetchall()


#CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT, analysis real)"
CREATE_TABLE_VIDEO = '''CREATE TABLE IF NOT EXISTS entries
                    (content TEXT, date TEXT)'''


CREATE_ENTRY_VIDEO = "INSERT INTO entries VALUES (?, ?)"
RETRIEVE_ENTRIES_VIDEO = "SELECT * FROM entries"


def create_table_video():
    with sqlite3.connect("data_video.db") as connection:
        connection.execute(CREATE_TABLE_VIDEO)


def create_entry_video(content, date):
    with sqlite3.connect("data_video.db") as connection:
        connection.execute(CREATE_ENTRY_VIDEO, (content, date))


def retrieve_entries_video():
    with sqlite3.connect("data_video.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES_VIDEO)
        return cursor.fetchall()
