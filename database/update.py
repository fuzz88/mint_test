"""
https://data.mos.ru/opendata/7704111479-svedeniya-o-naibolee-populyarnyh-mujskih-imenah-sredi-novorojdennyh?versionNumber=2&releaseNumber=99

https://data.mos.ru/opendata/7704111479-svedeniya-o-naibolee-populyarnyh-jenskih-imenah-sredi-novorojdennyh

gender: 1 for a man, 2 for a woman
"""

import csv
import sqlite3

db = sqlite3.connect("names.db")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS names;")


cursor.execute("CREATE TABLE names (name VARCHAR(64), gender INTEGER);")

with open("utf-8-data-6269-2022-04-13.csv") as females:
    data = csv.reader(females, delimiter=";")
    for row in data:
        cursor.execute("INSERT INTO names VALUES (?, ?)", (row[1], 2))

with open("utf-8-data-6271-2022-04-13.csv") as males:
    data = csv.reader(males, delimiter=";")
    for row in data:
        cursor.execute("INSERT INTO names VALUES (?, ?)", (row[1], 1))

db.close()
