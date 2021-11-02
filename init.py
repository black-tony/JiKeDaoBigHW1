import random

import flask
from flask import request, render_template, redirect, session, url_for
from flask_socketio import SocketIO, emit, disconnect

import Myconstants
from DatabassTool import MysqlUtil

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
                socketio.emit("login_response", {"error_code": findResult}, namespace='/login')
                return render_template("Login_new.html")
            # 找到暂时先转到生成的网页
            session['username'] = userName
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
                socketio.emit("register_response", {"error_code": 1})
                return
            # 没找到就可以插入数据库
            db = MysqlUtil()
            tmpDict = {Myconstants.USER_NAME: f'"{userName}"',
                       Myconstants.USER_PSWD: f'"{passWord}"',
                       Myconstants.USER_RANK: 1,
                       Myconstants.USER_MAIL: '"null@null.com"'
                       }
            db.insert(Myconstants.TABLE_USER_INFO, tmpDict)
        return redirect("/login")


@app.route('/index', methods=['GET'])
def mainPage():
    # 没有登录就转到登录界面
    if not ('username' in session):
        return redirect('/login')

    # TODO:根据内容确定, 感觉应该不会需要post协议
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

        videoUrl = request.args["video_url"]
        videoName = request.args['video_name']
        __output(videoUrl, videoName)
        return render_template('playvideo.html', video_url=videoUrl, video_name=videoName)


@socketio.on('disconnect', namespace='/login')
def onDisconnect():
    disconnect()


@socketio.on('get_animation')
def getAnimation(message):
    __output(message)
    needNum = message['need_video_nums']

    # 查询数据库, 拿到message条信息
    db = MysqlUtil()
    result = db.fetchall(Myconstants.TABLE_VIDEO_INFO,
                         f"{Myconstants.VIDEO_CATE}='{Myconstants.VIDEO_CATE_CACHE[1]}'")
    random.shuffle(result)
    ret = []
    for i in range(1, needNum + 1, 1):
        ret.append(result[i])
    emit("get_animation", {"videoInfos": ret})

    # 返回信息, 按照如下格式
    # {"videoInfos" : [ {videoUrl:val, videoName:val, videoGraph:val}, [], [], [], []] }
    # videoGraph: ./static/XXX.png


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


if __name__ == "__main__":
    socketio.run(app, debug=True)
    # app.run(debug=True)
