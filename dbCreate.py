import sqlite3
import vars

with sqlite3.connect('db') as cnn:
    cursor = cnn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS paths (path,status)")

    importPathsSql = "INSERT INTO paths(path,status) VALUES (?,?)"

    with open(vars.folder) as f:
        content = f.read().splitlines()


    for i in content:
        n = (i, 'false')
        cursor.execute(importPathsSql, n)

    cnn.commit()
