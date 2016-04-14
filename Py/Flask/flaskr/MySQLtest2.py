#!/usr/bin/python
#-*-coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25) )")
    cur.execute("INSERT INTO Writers(Name) VALUES('김민성')")
    cur.execute("INSERT INTO Writers(Name) VALUES('최명원')")
    cur.execute("INSERT INTO Writers(Name) VALUES('송혜민')")

