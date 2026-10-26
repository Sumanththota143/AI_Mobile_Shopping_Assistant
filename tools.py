import sqlite3

def connection():
    conn = sqlite3.connect("mobiles.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return cursor, conn

def clm_names():
    cursor, conn = connection()
    cursor.execute("SELECT * FROM mobiles")
    res = cursor.fetchone()
    names = res.keys()
    return names
    conn.close()

def fetch_by_id(item_id):
    cursor, conn = connection()
    cursor.execute("SELECT COUNT(*) FROM mobiles")
    total = cursor.fetchone()[0]
    print(f"---we have total: {total} mobiles---")
    cursor.execute("SELECT * FROM mobiles WHERE id = ?", (item_id,))
    record = cursor.fetchone()
    if not record:
        print("Data not found!")
        return
    data = []
    for i in record:
        data.append(i)
    names = clm_names()
    for i,j in zip(names,data):
        print(f"{i} : {j}")

fetch_by_id(39)
