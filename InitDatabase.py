import os

import pymysql
import Myconstants

host = Myconstants.HOST_CONST
user = Myconstants.USER_CONST
port = Myconstants.PORT_CONST
password = Myconstants.PASSWORD_CONST
database = Myconstants.DATABASE_CONST

#
# def __createTable(tableName, tableInfo, primaryKey):
#     db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
#     cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
#     sqlOrder = "CREATE TABLE IF NOT EXISTS " + f'{tableName}' + " ("
#     notFirst = 0
#     for key, value in tableInfo.items():
#         if notFirst == 0:
#             notFirst = 1
#         else:
#             sqlOrder += ", "
#         sqlOrder += f"{key} {value} NOT NULL"
#     if primaryKey:
#         sqlOrder += ', PRIMARY key('
#         notFirst = 0
#         for i in primaryKey:
#             if notFirst == 0:
#                 notFirst = 1
#             else:
#                 sqlOrder += ", "
#             sqlOrder += f'{i}'
#         sqlOrder += ")"
#     sqlOrder += ");"
#     # print(sqlOrder)
#     cursor.execute(sqlOrder)
#     db.commit()
#     cursor.close()
#     db.close()


# sqlOrder = "CREATE TABLE IF NOT EXIST " + Myconstants.TABLE_USER_INFO + " ("
# notFirst = 0
# for key, value in Myconstants.USER_INFO:
#     if notFirst == 0:
#         notFirst = 1
#     else:
#         sqlOrder += ", "
#     sqlOrder += f"'{key}' {value} NOT NULL"
# sqlOrder += ', PRIMARY key("userName"));'
# cursor.execute(sqlOrder)
# db.commit()
# __createTable(Myconstants.TABLE_USER_INFO, Myconstants.USER_INFO, Myconstants.PRIMARY_KEY_USER_INFO)
# __createTable(Myconstants.TABLE_DANMAKU_INFO, Myconstants.DANMAKU_INFO, Myconstants.PRIMARY_KEY_DANMAKU_INFO)
# __createTable(Myconstants.TABLE_VIDEO_INFO, Myconstants.VIDEO_INFO, Myconstants.PRIMARY_KEY_VIDEO_INFO)

os.system(f"mysql -u{user} -p{password} < Db_1106.sql")