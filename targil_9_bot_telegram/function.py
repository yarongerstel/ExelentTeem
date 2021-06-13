import sympy
import math

TOKEN = '1840585621:AAEy1RoiM8wdJTnUe3OlhxRfeAHzDLPg-9Y'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://f60156e783e1.ngrok.io/message' \
    .format(TOKEN)


def isprime(num):
    msg = ""
    if num == 2:
        msg = "Come on dude, you know even numbers are not prime!"
    elif sympy.isprime(num):
        msg = "prime"
    else:
        msg = "not prime"
    return msg


def ispalindrome(num):
    msg = ""
    if str(num) == str(num)[::-1]:
        msg = "palindrome"
    else:
        msg = "not palindrome"
    return msg


def issqrt(num):
    msg = ""
    if math.sqrt(num).is_integer():
        msg = "sqrt"
    else:
        msg = "not sqrt"
    return msg


def isfactorial(num):
    check=1
    for i in range(1,num+1):
        if check*i <= num:
            check*=i
    if check == num:
        return "factorial"
    else:
        return "not factorial"