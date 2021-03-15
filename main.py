import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = '1634180311:AAGCvsGzDN9iEGEnJYCjVjWwQiagdHgvAa4'

def parser(text, url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    a = ""
    for item in soup.find_all("b"):
        if item.contents[0].find(text) == 0:
            a = item.parent['href']
            return a


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Place request type: 'Author (FIO)/Book name' (for example 'Пушкин Александр Сергеевич/Евгений Онегин'")
    bot.reply_to(message, "made by PlzD0ntcry")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        arr = message.text.split("/")
        url = "http://lib.ru/LITRA/"
        print(arr[1])
        auth = parser(arr[0], url)
        print(auth)
        try:
            url1 = url+auth
            a = requests.get(url1+parser(arr[1], url1)).text
            print(a)

        except:
            url1=auth
            a = requests.get(url1 + parser(arr[1], url1)).text
            print(a)
        b=a[6:]
        parts = [b[i:i + 4095] for i in range(0, len(b), 4095)]
        bot.reply_to(message, "<a href='{}'>here's it</a>".format(url1 + parser(arr[1], url1)), parse_mode='HTML')
    except:
        bot.reply_to(message, "input incorrect or book not found, please follow instruction given above or call /start")

bot.polling()

if __name__ == '__main__':
    bot = telebot.TeleBot(TOKEN)
    print("started")
    bot.polling()


