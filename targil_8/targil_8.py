from flask import Flask, request, redirect, url_for, session
from markupsafe import escape
from tinydb import TinyDB, Query

db = TinyDB(r'C:\Users\USER001\PycharmProjects\ExelentTeem\targil_8\db.json')
User = Query()


app = Flask(__name__)
users = []

app.secret_key = b'hgfhgfj\n\xec'


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if 'username' in session:
        return "welcom %s" % escape(session['username'])
    else:
        return "you are not login in.."


@app.route('/login', methods=["GET", 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        #  users.append(request.form['username'])
        return redirect(url_for('home_page'))

    return '''<form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
              </form>'''


@app.route('/logout')
def logoutkl():
    session.pop('username')
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(host="localhost", port=9003, debug=True)
