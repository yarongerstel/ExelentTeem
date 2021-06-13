from view import *

if __name__ == '__main__':
    requests.get(function.TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=5002)
