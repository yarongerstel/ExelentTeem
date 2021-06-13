from flask import Flask, request, redirect, url_for, session
from markupsafe import escape
import controller

app = Flask(__name__)
app.secret_key = b'hgfhgfj\n\xec'


@app.route('/')
def home_page():
    if 'username' in session:
        return """
                <p>Welcome %s </p>
        """ % escape(session['username'])
    else:
        return "you are not login in.."


@app.route('/login', methods=["GET", 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        session['username'] = name
        #  users.append(request.form['username'])
        try:
            return redirect(url_for('home_page'))
        except Exception as e:
            return e

    return '''<form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
              </form>'''


@app.route('/logout')
def logoutkl():
    session.pop('username')
    try:
        return redirect(url_for('home_page'))
    except Exception as e:
        return e


@app.route('/insights')
def insights():
    try:
        return str(controller.Controller.get_all())
    except Exception as e:
        return e


@app.route('/insight', methods=['GET', 'POST'])
def insight():
    if request.method == 'POST':
        user_in = request.form['content']
        try:
            controller.UserController.create_user(session['username'], user_in)
            return "don!"
        except Exception as e:
            return e
    return '''<form method="post">
                        <p><input type=text name=content>
                        <p><input type=submit value=POST>
                      </form>'''


@app.route('/republish', methods=['GET', 'POST'])
def republish():
    if request.method == 'POST':
        insight_id = request.form['id']
        try:
            return str(controller.UserController.republish(insight_id, session['username']))
        except Exception as e:
            return e

    return '''<form method="post">
                            <p><input type=text name=id>
                            <p><input type=submit value=update>
                          </form>'''


@app.route('/mostpublish')
def mostpublish():
    try:
        return str(controller.Controller.get_most_publish())
    except Exception as e:
        return e
