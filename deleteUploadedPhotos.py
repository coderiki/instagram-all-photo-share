import os
import sqlite3



with sqlite3.connect('db') as cnn:
    cursor = cnn.cursor()
    cursor.execute("SELECT rowid,* FROM {} WHERE status = '{}' AND existsStatus = '{}'".format('paths', 'true', 'true'))
    updatePathsSql = "UPDATE paths SET existsStatus = ? WHERE _rowid_ = ?"
    datas = cursor.fetchall()
    for i in datas:
        os.remove(i[1])
        m = ("false", i[0])
        cursor.execute(updatePathsSql, m)