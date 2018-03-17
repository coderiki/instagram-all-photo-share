import sqlite3
import vars

with sqlite3.connect('db') as cnn:
    cursor = cnn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS paths (path,status,existsStatus)")

    importPathsSql = "INSERT INTO paths(path,status,existsStatus) VALUES (?,?,?)"

    with open(vars.folder) as f:
        content = f.read().splitlines()


    for i in content:
        n = (i, 'false','true')
        cursor.execute(importPathsSql, n)

    cnn.commit()
