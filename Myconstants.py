HOST_CONST = "localhost"
USER_CONST = "root"
PORT_CONST = 3306
PASSWORD_CONST = "Gz8ymJMXfbr#3*5"
DATABASE_CONST = "bigHW1"

TABLE_USER_INFO = "usersinfo"
PRIMARY_KEY_USER_INFO = ["userName"]
USER_INFO = {
    "userName": "varchar(50)",
    "userPswd": "varchar(50)",
    "userRank": "int unsigned",
    "userMail": "varchar(50)"
}
USER_NAME = "userName"
USER_PSWD = "userPswd"
USER_RANK = "userRank"
USER_MAIL = "userMail"

TABLE_DANMAKU_INFO = "danmakuinfo"
PRIMARY_KEY_DANMAKU_INFO = []
DANMAKU_INFO = {
    "danmakuContent": "varchar(100)",
    "danmakuTimeAxis": "int unsigned",
    "danmakuUser": "varchar(50)"
}
D_CONTENT = "danmakuContent"
D_TIMEAXIS = "danmakuTimeAxis"
D_USER = "danmakuUser"


TABLE_VIDEO_INFO = "videoinfo"
PRIMARY_KEY_VIDEO_INFO = ["videoUrl"]
VIDEO_INFO = {
    "videoUrl": "varchar(100)",
    "videoGraph": "varchar(100)",
    "videoName": "varchar(100)"
}
VIDEO_URL = "videoUrl"
VIDEO_GRAPH = "videoGraph"
VIDEO_NAME = "videoName"





