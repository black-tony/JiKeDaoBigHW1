import random

import flask
from flask import request, render_template, redirect, session, url_for
from flask_socketio import SocketIO, emit, disconnect

from pythonfile import Myconstants
from pythonfile.DatabassTool import MysqlUtil

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "r`9[M-AtuO"
socketio = SocketIO(app, async_mode=None)


def __output(*message):
    if Myconstants.DEBUG:
        print(message)


# 现在是运行起来之后,http://127.0.0.1:5000/ 这里可以看到html的内容了
@app.route('/', methods=['GET'])
def website():
    if request.method == 'GET':
        return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 已经登录, 禁止继续登录
    if 'username' in session:
        return redirect('/index')

    if request.method == 'GET':
        return render_template("Login_new.html")
    else:
        userName = request.form['username']
        passWord = request.form['password']
        # 链接数据库查询
        if userName and passWord:
            db = MysqlUtil()
            result = db.fetchone(Myconstants.TABLE_USER_INFO,
                                 f'{Myconstants.USER_NAME}="{userName}"',
                                 Myconstants.USER_PSWD, Myconstants.USER_RANK)
            # 没查找到暂时先转回原网页
            findResult = 0
            if not result:
                findResult = 1
            elif passWord != result[Myconstants.USER_PSWD]:
                findResult = 2
            if findResult > 0:
                # socketio.emit("login_response", {"error_code": findResult})
                __output(findResult)
                session['login_fail'] = findResult
                return redirect("/login")
            # 找到暂时先转到生成的网页
            session['username'] = userName
            session['level'] = result[Myconstants.USER_RANK]
            # express = f"<h2>hello !{userName} </h2><h2>Your password is {passWord}!</h2>" + \
            #          f"<h2>Your Rank Is {result[Myconstants.USER_RANK]}</h2>"
            # return express
            if 'redirect_video' in session:
                if session['redirect_video']:
                    videoUrl = session['video_url']
                    videoName = session['video_name']
                    session.pop('video_url')
                    session.pop('video_name')
                    session.pop('redirect_video')
                    return redirect(url_for('playPage', video_url=videoUrl, video_name=videoName))
            else:
                return redirect(url_for('mainPage'))
        else:
            session['login_fail'] = 3
            return redirect("/login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 已经登录, 禁止继续登录
    if 'username' in session:
        return redirect('/index')

    if request.method == 'GET':
        return render_template("Register.html")
    else:
        userName = request.form['username']
        passWord = request.form['password']
        # 链接数据库查询
        if userName and passWord:
            db = MysqlUtil()
            result = db.fetchone(Myconstants.TABLE_USER_INFO,
                                 f'{Myconstants.USER_NAME}="{userName}" OR {Myconstants.USER_MAIL}="NULL"',
                                 Myconstants.USER_PSWD, Myconstants.USER_RANK)
            # username重复 或者email 重复
            if result:
                session["register_fail"] = 1
                # socketio.emit("register_response", {"error_code": 1})
                return redirect('/register')
            # 密码不够长, 返回重新写
            if len(passWord) < 6:
                session["register_fail"] = 3
                return redirect('/register')
            # 没找到就可以插入数据库
            db = MysqlUtil()
            tmpDict = {Myconstants.USER_NAME: f'"{userName}"',
                       Myconstants.USER_PSWD: f'"{passWord}"',
                       Myconstants.USER_RANK: 1,
                       Myconstants.USER_MAIL: '"null@null.com"'
                       }
            db.insert(Myconstants.TABLE_USER_INFO, tmpDict)
            return redirect("/login")
        else:
            session['register_fail'] = 2
            return redirect('/register')


@app.route('/index', methods=['GET'])
def mainPage():
    # 没有登录就转到登录界面
    if not ('username' in session):
        return redirect('/login')
    # getVideoNums(None)
    return render_template('/index.html', async_mode=socketio.async_mode)


@app.route('/play_video', methods=['GET'])
def playPage():
    # 没有登录就转到登录界面

    if request.method == 'GET':
        videoUrl = None
        videoName = None

        if not ('username' in session):
            session['redirect_video'] = True
            session['video_url'] = videoUrl
            session['video_name'] = videoName
            return redirect('/login')
        if not ('video_url' in request.args) or not ('video_name' in request.args):
            return redirect('/index')
        videoUrl = request.args["video_url"]
        videoName = request.args['video_name']
        __output(videoUrl, videoName)
        return render_template('playvideo.html', video_url=videoUrl, video_name=videoName)


@app.route('/animation')
def animationPage():
    return render_template('animation.html')


@app.route('/dance')
def dancePage():
    return render_template('dance.html')


@app.route('/life')
def lifePage():
    return render_template('life.html')


@app.route('/movie')
def moviePage():
    return render_template('movie.html')


@app.route('/music')
def musicPage():
    return render_template('music.html')


@app.route('/technology')
def technologyPage():
    return render_template('technology.html')


@app.route('/user_config')
def configUser():
    return render_template('user.html')


@app.route('/danmaku_config')
def configDanmaku():
    return render_template('plane.html')


@socketio.on('get_previous_login')
def getPreviousLogin():
    if "login_fail" in session:
        socketio.emit("login_response", {"error_code": session['login_fail']})
        session.pop('login_fail')


@socketio.on('get_previous_register')
def getPreviousRegister():
    if "register_fail" in session:
        socketio.emit("register_response", {"error_code": session['register_fail']})
        session.pop('register_fail')


@socketio.on('disconnect', namespace='/login')
def onDisconnect():
    disconnect()


@socketio.on("get_video_nums")
def getVideoNums():
    nameCount = []
    for i in Myconstants.VIDEO_CATE_CACHE:
        db = MysqlUtil()
        result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                             f"{Myconstants.VIDEO_CATE} = '{i}'",
                             Myconstants.VIDEO_NAME
                             )
        nameCount.append(len(result))
    __output(nameCount)
    emit("get_video_nums", {"num": nameCount})


@socketio.on('get_' + Myconstants.VIDEO_CATE_CACHE[1])
def getMusic(message):
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[1]}'")
    random.shuffle(result)
    ret = []
    if needNum != -1:
        for i in range(0, min(needNum, len(result)), 1):
            ret.append(result[i])
    else:
        ret = result
    emit('get_' + Myconstants.VIDEO_CATE_CACHE[1], {"videoInfos": ret, "count": len(ret)})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


@socketio.on('get_' + Myconstants.VIDEO_CATE_CACHE[2])
def getDance(message):
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[2]}'")
    random.shuffle(result)
    ret = []
    if needNum != -1:
        for i in range(0, min(needNum, len(result)), 1):
            ret.append(result[i])
    else:
        ret = result
    emit('get_' + Myconstants.VIDEO_CATE_CACHE[2], {"videoInfos": ret, "count": len(ret)})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


@socketio.on('get_' + Myconstants.VIDEO_CATE_CACHE[3])
def getTechnology(message):
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[3]}'")
    random.shuffle(result)
    ret = []
    if needNum != -1:
        for i in range(0, min(needNum, len(result)), 1):
            ret.append(result[i])
    else:
        ret = result
    emit('get_' + Myconstants.VIDEO_CATE_CACHE[3], {"videoInfos": ret, "count": len(ret)})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


@socketio.on('get_' + Myconstants.VIDEO_CATE_CACHE[4])
def getLife(message):
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[4]}'")
    random.shuffle(result)
    ret = []
    if needNum != -1:
        for i in range(0, min(needNum, len(result)), 1):
            ret.append(result[i])
    else:
        ret = result
    emit('get_' + Myconstants.VIDEO_CATE_CACHE[4], {"videoInfos": ret, "count": len(ret)})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


@socketio.on('get_' + Myconstants.VIDEO_CATE_CACHE[5])
def getMovie(message):
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[5]}'")
    __output(result)
    random.shuffle(result)
    __output(result)
    ret = []
    if needNum != -1:
        for i in range(0, min(needNum, len(result)), 1):
            ret.append(result[i])
    else:
        ret = result
    __output(ret)
    emit('get_' + Myconstants.VIDEO_CATE_CACHE[5], {"videoInfos": ret, "count": len(ret)})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


@socketio.on('get_' + Myconstants.VIDEO_CATE_CACHE[0])
def getAnimation(message):
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[0]}'")
    random.shuffle(result)
    ret = []
    if needNum != -1:
        for i in range(0, min(needNum, len(result)), 1):
            ret.append(result[i])
    else:
        ret = result
    emit('get_' + Myconstants.VIDEO_CATE_CACHE[0], {"videoInfos": ret, "count": len(ret)})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


# {
# 'danmu_text': 'asdasd',
# 'danmu_color': '#ffffff',
# 'danmu_size': '1',
# 'danmu_position': '0',
# 'danmu_time': 21,
# 'danmu_userid': 'root'
# 'danmu_video': 'name'
# }
@socketio.on('send_danmu')
def receiveDanmaku(message):
    # __output(message)
    db = MysqlUtil()

    danmakuInfo = {
        Myconstants.D_POS: message['danmu_position'],
        Myconstants.D_TEXT: f"'{message['danmu_text']}'",
        Myconstants.D_TIME: message['danmu_time'],
        Myconstants.D_USER: f"'{message['danmu_userid']}'",
        Myconstants.D_SIZE: message['danmu_size'],
        Myconstants.D_COLOR: f"'{message['danmu_color']}'",
        Myconstants.D_VIDEO: f"'{message['danmu_video']}'"
    }
    db.insert(Myconstants.TABLE_DANMAKU_INFO, danmakuInfo)


@socketio.on('get_userid')
def getUserId():
    emit('get_userid', {'id': session['username']})


@socketio.on('get_danmu')
def sendDanmaku(message):
    db = MysqlUtil()
    curDanmaku = db.fetchall(table=Myconstants.TABLE_DANMAKU_INFO,
                             condition=f"{Myconstants.D_VIDEO}='{message['danmu_video']}'")
    # data.danmuinfo[i]包含content(string类型),
    # color(string类型，存储的时候包含#),
    # fontsize,
    # position,
    # time五个参数
    retDanmaku = []
    for i in curDanmaku:
        curInfo = {
            "content": i[Myconstants.D_TEXT],
            "color": i[Myconstants.D_COLOR],
            "fontsize": i[Myconstants.D_SIZE],
            "position": i[Myconstants.D_POS],
            "time": i[Myconstants.D_TIME]
        }
        retDanmaku.append(curInfo)
    emit('get_danmu', {'num': len(curDanmaku), "danmuinfo": retDanmaku})


@socketio.on('get_userlist')
def returnUserList():
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_USER_INFO)
    retList = []
    for i in result:
        tmpUser = {
            "name": i[Myconstants.USER_NAME],
            "password": i[Myconstants.USER_PSWD]
        }
        retList.append(tmpUser)
    emit('get_userlist', {"count": len(retList), "user": retList})


@socketio.on('delete_user')
def deleteUser(message):
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_USER_INFO)
    orderPlace = int(message['place'])
    if len(result) >= orderPlace:
        userInfo = result[orderPlace - 1]
        if session['level'] > userInfo[Myconstants.USER_RANK]:
            ndb = MysqlUtil()
            ndb.delete(Myconstants.TABLE_USER_INFO, f"{Myconstants.USER_NAME}='{userInfo[Myconstants.USER_NAME]}'")


@socketio.on('get_danmulist')
def getDanmaku():
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_DANMAKU_INFO)
    retList = []
    for i in result:
        tmpD = {
            "videoname": i[Myconstants.D_VIDEO],
            "time": i[Myconstants.D_TIME],
            "user": i[Myconstants.D_USER],
            "content": i[Myconstants.D_TEXT]
        }
        retList.append(tmpD)
    emit('get_danmulist', {"count": len(retList), "danmu": retList})


@socketio.on('delete_danmu')
def deleteDanmaku(message):
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_DANMAKU_INFO)
    orderPlace = int(message['place'])
    if len(result) >= orderPlace:
        DInfo = result[orderPlace - 1]
        if session['level'] > 1:
            ndb = MysqlUtil()
            ndb.delete(Myconstants.TABLE_DANMAKU_INFO, f"{Myconstants.D_ID}={DInfo[Myconstants.D_ID]}")


@socketio.on('get_usergrade')
def getUsergrade():
    grade = -1
    if session['level'] > 1:
        grade = 1
    else:
        grade = 0
    emit("get_usergrade", {"grade": grade})


if __name__ == "__main__":
    socketio.run(app)
    # app.run(debug=True)
