import sqlite3

def connect_db():
    """Connects to the SQLite3 database"""
    conn = sqlite3.connect("contacts_data.db")
    return conn



if __name__ == '__main__':
    conn = connect_db()
    cur = conn.cursor()
    #cur.execute("pragma table_info(contacts)")
    cur.execute("select rowid from contacts")
    data = cur.fetchall()
    print(data)

    conn.commit()
    conn.close()