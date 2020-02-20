import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE tab (id INTEGER PRIMARY KEY, name TEXT);")
tab_name = ['A', 'B', 'C']
cur.executemany("INSERT INTO tab (name) VALUES (?)", tab_name)

cur.execute("SELECT * FROM tab")
print(cur.fetchall())
for row in cur.execute("SELECT rowid, * FROM tab"):
    print(row)