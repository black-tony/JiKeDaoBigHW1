HOST_CONST = "localhost"
USER_CONST = "root"
PORT_CONST = 3306
PASSWORD_CONST = "Gz8ymJMXfbr#3*5"
DATABASE_CONST = "bigHW1"
DEBUG = True
TABLE_USER_INFO = "usersinfo"
PRIMARY_KEY_USER_INFO = ["userName"]
USER_INFO = {
    "userName": "varchar(50)",
    "userPswd": "varchar(50)",
    "userRank": "int unsigned",
    "userMail": "varchar(50)",
}
USER_NAME = "userName"
USER_PSWD = "userPswd"
USER_RANK = "userRank"
USER_MAIL = "userMail"

TABLE_DANMAKU_INFO = "danmakuinfo"
PRIMARY_KEY_DANMAKU_INFO = ["danmukuId"]
DANMAKU_INFO = {
    "danmakuText": "varchar(100)",
    "danmakuColor": "varchar(10)",
    "danmakuSize": "int, unsigned",
    "danmukuPos": 'int unsigned',
    "danmukuTime": 'int unsigned',
    "danmukuUser": 'varchar(50)',
    "danmukuVideo": "varchar(100)",
    "danmukuId": "int unsigned AUTO_INCREASE"
}
D_TEXT = "danmakuText"
D_TIME = "danmakuTime"
D_USER = "danmakuUser"
D_COLOR = "danmakuColor"
D_SIZE = "danmakuSize"
D_POS = "danmukuPos"
D_VIDEO = "danmukuVideo"
D_ID = "danmukuId"

TABLE_VIDEO_INFO = "videoinfo"
PRIMARY_KEY_VIDEO_INFO = ["videoUrl"]
VIDEO_INFO = {
    "videoUrl": "varchar(100)",
    "videoGraph": "varchar(100)",
    "videoName": "varchar(100)",
    "videoCate": "varchar(100)"
}
VIDEO_URL = "videoUrl"
VIDEO_GRAPH = "videoGraph"
VIDEO_NAME = "videoName"
VIDEO_CATE = "videoCate"
VIDEO_CATE_CACHE = [
    "animation",
    "music",
    "dance",
    "technology",
    "life",
    "movie"
]





