import pymysql

HOST_CONST = "localhost"
USER_CONST = "root"
PORT_CONST = 3306
PASSWORD_CONST = "Gz8ymJMXfbr#3*5"
DATABASE_CONST = "test_db"
TABLE_CONST = "employee"

host = HOST_CONST
user = USER_CONST
port = PORT_CONST
password = PASSWORD_CONST
database = DATABASE_CONST
db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
TABLE_USER_INFO = "usersinfo"
USER_INFO = {
    "userName": "varchar(50)",
    "userPswd": "varchar(50)",
    "userRank": "int unsigned",
    "userMail": "varchar(50)"
}

sqlOrder = "CREATE TABLE IF NOT EXIST " + TABLE_USER_INFO + " ("
notFirst = 0
for key, value in USER_INFO:
    if notFirst == 0:
        notFirst = 1
    else:
        sqlOrder += ", "
    sqlOrder += f"'{key}' {value} NOT NULL"
sqlOrder += ', PRIMARY key("userName"));'
cursor.execute(sqlOrder)
db.commit()




