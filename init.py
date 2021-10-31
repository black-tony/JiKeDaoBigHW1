import flask
from flask import request, render_template, redirect

import Myconstants
from DatabassTool import MysqlUtil

app = flask.Flask(__name__)


# 现在是运行起来之后,http://127.0.0.1:5000/ 这里可以看到html的内容了
@app.route('/', methods=['GET'])
def website():
    if request.method == 'GET':
        return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
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
            if not result or passWord != result[Myconstants.USER_PSWD]:
                return redirect("/login")
            # 找到暂时先转到生成的网页
            express = f"<h2>hello !{userName} </h2><h2>Your password is {passWord}!</h2>" + \
                      f"<h2>Your Rank Is {result[Myconstants.USER_RANK]}</h2>"
            return express
        return redirect("/login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("Register.html")
    else:
        userName = request.form['username']
        passWord = request.form['password']
        # 链接数据库查询
        if userName and passWord:
            db = MysqlUtil()
            result = db.fetchone(Myconstants.TABLE_USER_INFO,
                                 f'{Myconstants.USER_NAME}="{userName} OR {Myconstants.USER_MAIL}="NULL"',
                                 (Myconstants.USER_PSWD, Myconstants.USER_RANK))
            # username重复 或者email 重复
            if result:
                return redirect("/register")
            # 没找到就可以插入数据库
            db = MysqlUtil()
            tmpDict = {Myconstants.USER_NAME: userName,
                       Myconstants.USER_PSWD: passWord,
                       Myconstants.USER_RANK: 1,
                       Myconstants.USER_MAIL: "null@null.com"
                       }
            db.insert(Myconstants.TABLE_USER_INFO, tmpDict)
        return redirect("/login")


app.run(debug=True)
