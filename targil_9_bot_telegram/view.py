from flask import Flask, request, Response, url_for
import requests
import function
import db

app = Flask(__name__)

requests.get(function.TELEGRAM_INIT_WEBHOOK_URL)


@app.route("/")
def root():
    return "server is running.."


@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    chat_id = request.get_json()['message']['chat']['id']
    answer = request.get_json()['message']['text']
    try:
        listmsg = (answer.split(" "))
        order = listmsg[0]
        if order == "max_number":
            answer = db.NumberModelWrapper.get_max_number_count()
        elif int(listmsg[1]):
            db.NumberModelWrapper.create(listmsg[1])  # creat or add 1 to the amount
        if order == "prime":
            answer = function.isprime(int(listmsg[1]))
        elif order == "palindrome":
            answer = function.ispalindrome(int(listmsg[1]))
        elif order == "sqrt":
            answer = function.issqrt(int(listmsg[1]))
        elif order == "factorial":
            answer = function.isfactorial(int(listmsg[1]))
        elif order == "max_number":
            answer = db.NumberModelWrapper.get_max_number_count()
    except Exception as e:
        answer = e

    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(function.TOKEN, chat_id, (str(answer))))
    return Response("success")

