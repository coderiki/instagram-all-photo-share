from InstagramAPI import InstagramAPI
import time
import vars
import sqlite3

InstagramAPI = InstagramAPI(vars.login, vars.password)
InstagramAPI.login()

with sqlite3.connect('db') as cnn:
    cursor = cnn.cursor()
    cursor.execute("SELECT rowid,* FROM {} WHERE status = '{}'".format('paths', 'false'))
    updatePathsSql = "UPDATE paths SET status = ? WHERE _rowid_ = ?"
    datas = cursor.fetchall()
    print(datas)
    # exit()
    for i in datas:
        photo_path = i[1]
        caption = ""  # açıklama girmek istersen burada belirtirsin hocam.
        InstagramAPI.uploadPhoto(photo_path, caption=caption)
        m = ("true", i[0])
        cursor.execute(updatePathsSql, m)
        # print("{} id li path paylaşıldı.".format(i[0]))
        continue
        time.sleep(vars.sleep)








