import flask
from flask import request, render_template

app = flask.Flask(__name__)


# 现在是运行起来之后,http://127.0.0.1:5000/ 这里可以看到html的内容了
@app.route('/')
def website():
    return render_template("website.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # under development
        userName = request.form['userName']
        passWord = request.form['passWord']
        return f"<h2>hello !{userName} </h2><h2>Your password is {passWord}!</h2>"


app.run(debug=True)
