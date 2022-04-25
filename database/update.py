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
cursor.execute("DROP TABLE IF EXISTS second_names")

# не оптимально, но повторы имён будем убирать с помощью унрикальности элементов сета
unique_names = set()

cursor.execute("CREATE TABLE names (name, gender)")
cursor.execute("CREATE TABLE second_names (second_name, gender)")

with open("utf-8-data-6269-2022-04-13.csv") as females:
    data = csv.reader(females, delimiter=";")
    for row in data:
        # убираем битые имена, начинающиеся с маленькой буквы
        if row[1][0:1] != str(row[1][0:1]).upper():
            continue
        # также в данных есть варианты имени через запятую-пробел. учтём варианты.
        for name in row[1].split(", "):
            unique_names.add(name)
    for name in unique_names:
        cursor.execute("INSERT INTO names VALUES (?, ?)", (name, 2))

unique_names = set()

with open("utf-8-data-6271-2022-04-13.csv") as males:
    data = csv.reader(males, delimiter=";")
    for row in data:
        if row[1][0:1] != str(row[1][0:1]).upper():
            continue
        for name in row[1].split(", "):
            unique_names.add(name)
    for name in unique_names:
        cursor.execute("INSERT INTO names VALUES (?, ?)", (name, 1))

with open("second_name_balanovskaya_top50.txt") as second_names:
    for second_name in second_names.readlines():
        second_name = second_name.strip()
        # женская фамилия, согласно нашему простому списку, это мужская плюс "а" в конце
        values = [(second_name, 1), (second_name + "а", 2)]
        cursor.executemany("INSERT INTO second_names VALUES (?, ?)", values)

db.commit()
cursor.close()
db.close()
