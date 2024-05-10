#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import os
import json

API_TOKEN = None

bot = telebot.TeleBot(API_TOKEN,  parse_mode=None)
check_equipos = None

def ping(host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        print(host, 'is up!')
        return True
    else:
        print(host, 'is down!')
        return False


def buscar_equipos():
    with open('equipos.json') as f:
        data = json.load(f)

    return data.get("equipos", {})

def check_equipo(e):
        # print(f"E = {e}")
        try:
            message = ''
            
            name = e["name"]
            ip = e['ip']
            if ping(ip):
                    message = f"{name} UP 🟩\n"
                    e["state"] = True
                    print(e)
            else:
                    message = f"{name} DOWN 🟥\n"
                    e["state"] = False
                    print(e)

            return message
        except Exception as e:
            print(e)
            pass


def do_ping(equipos):
    while True:
        msg = '\n'
        for e in equipos:
            print(f"{e}")
            msg += check_equipo(e)
        return msg
        # time.sleep(15)
        # print('-------------------------------\n')

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print(f"message {message}")
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
# Handle '/start' and '/help'
@bot.message_handler(commands=['status'])
def send_status1(message):
    global check_equipos

    if not check_equipos:
         check_equipos = buscar_equipos()

    bot.reply_to(message, "Aguantalo menol")
    msg = (do_ping(check_equipos))
    bot.reply_to(message, msg)


# Handle 'status'
# @bot.edited_channel_post_handler(['run'])
@bot.channel_post_handler(['run'])
def send_status(message):
    global check_equipos

    if not check_equipos:
         check_equipos = buscar_equipos()

    bot.reply_to(message, "Aguantalo 5 min menol!!!!")
    msg = (do_ping(check_equipos))
    bot.reply_to(message, msg)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # print(message.chat.type)
    if message.chat.type == 'channel':
        if '@echobot' in message.text:
            bot.send_message(message.chat.id, message.text.replace('@echobot', ''))
    else:
        bot.reply_to(message, message.text)


def main():
     bot.infinity_polling()

if __name__ == "__main__":
    main()
