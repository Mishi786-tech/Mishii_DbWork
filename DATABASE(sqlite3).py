# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:42:32 2025

@author: L1F22PACS0008
"""

import sqlite3
print(sqlite3.sqlite_version)

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

#create table if it doesn't exist
cursor.execute("""
               CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER
                   )""")
conn.commit()


cursor.execute("INSERT INTO user(name,age) VALUES (?,?)",("Alice",25))
cursor.execute("INSERT INTO user(name,age) VALUES (?,?)",("Bob",30))
conn.commit()

cursor.execute("SELECT * FROM user")
rows= cursor.fetchall()
print("\nUser after INSERT:")
for row in rows:
    print(row)
    
cursor.execute("UPDATE user SET age = ? WHERE name = ?",(28,"Alice"))
conn.commit()    

cursor.execute("SELECT * FROM  user")
rows = cursor.fetchall()
print("\nUser after update:")
for row in rows:
    print(row)

cursor.execute("DELETE FROM user WHERE name =?" , ("Bob",))
conn.commit()

cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()
print("\nUser after DELETE:")
for row in rows: 
    print(row)

conn.close() 
   
    