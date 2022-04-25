"""
https://data.mos.ru/opendata/7704111479-svedeniya-o-naibolee-populyarnyh-mujskih-imenah-sredi-novorojdennyh?versionNumber=2&releaseNumber=99

https://data.mos.ru/opendata/7704111479-svedeniya-o-naibolee-populyarnyh-jenskih-imenah-sredi-novorojdennyh

gender: 1 for a man, 2 for a woman
"""

import csv
import sqlite3

db = sqlite3.connect("names.db")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS names")

# не оптимально, но повторы имён будем убирать с помощью унрикальности элементов сета
unique_names = set()

cursor.execute("CREATE TABLE names (name, gender) ")

with open("utf-8-data-6269-2022-04-13.csv") as females:
    data = csv.reader(females, delimiter=";")
    for row in data:
        if row[1][0:1] != str(row[1][0:1]).upper():
            # убираем битые имена, начинающиеся с маленькой буквы
            continue
        unique_names.add(row[1])
    print(unique_names)
    for name in unique_names:
        cursor.execute("INSERT INTO names VALUES (?, ?)", (name, 2))

unique_names = set()

with open("utf-8-data-6271-2022-04-13.csv") as males:
    data = csv.reader(males, delimiter=";")
    for row in data:
        if row[1][0:1] != str(row[1][0:1]).upper():
            continue
        unique_names.add(row[1])
    print(unique_names)
    for name in unique_names:
        cursor.execute("INSERT INTO names VALUES (?, ?)", (name, 1))

db.commit()
cursor.close()
db.close()
