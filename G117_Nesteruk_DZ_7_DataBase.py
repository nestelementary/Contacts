import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("""CREATE TABLE worker
            (worker_id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             date_of_birth TEXT NOT NULL,
             address TEXT NOT NULL,
             phone INTEGER NOT NULL)""")
cur.execute("""CREATE TABLE position
            (position_id INTEGER PRIMARY KEY,
             worker_id INTEGER NOT NULL,
             name TEXT NOT NULL,
             position TEXT NOT NULL,
             FOREIGN KEY (worker_id) REFERENCES worker (worker_id))""")
cur.execute("""CREATE TABLE salary
            (salary_id INTEGER PRIMARY KEY,
             worker_id INTEGER NOT NULL,
             net_salary REAL NOT NULL,
             tax REAL NOT NULL,
             FOREIGN KEY (worker_id) REFERENCES worker (worker_id))""")
worker = [('1001', 'John First', '01012001', 'City', '111'),
          ('1002', 'Jane Second', '01012002', 'Town', '112'),
          ('1003', 'Thom Third', '01012003', 'Village', '113'),
          ('1004', 'Ann Fourth', '01012004', 'County', '114'),
          ('1005', 'Bill Fifth', '01012005', 'Country', '115')]
cur.executemany("INSERT INTO worker VALUES (?,?,?,?,?)", worker)
position = [('1001', 'John First', 'driver'),
            ('1002', 'Jane Second', 'secretary'),
            ('1003', 'Thom Third', 'accountant'),
            ('1004', 'Ann Fourth', 'lawyer'),
            ('1005', 'Bill Fifth', 'chief')]
cur.executemany("INSERT INTO position (worker_id, name, position) VALUES (?,?,?)", position)
salary = [('1001', '10,0', '2,0'),
            ('1002', '12,5', '2,5'),
            ('1003', '16,0', '3,2'),
            ('1004', '18,0', '3,6'),
            ('1005', '20,0', '4,0')]
cur.executemany("INSERT INTO salary (worker_id, net_salary, tax) VALUES (?,?,?)", salary)
con.commit()
print("Worker data:")
rows = cur.execute("SELECT * FROM worker")
print([rows[0] for rows in cur.description])
for row in rows:
    print(row)
print("Position data:")
rows = cur.execute("SELECT * FROM position")
print([rows[0] for rows in cur.description])
for row in rows:
    print(row)
print("Salary data:")
rows = cur.execute("SELECT * FROM salary")
print([rows[0] for rows in cur.description])
for row in rows:
    print(row)
con.close()
