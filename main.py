import os
import telebot
import random
from userManagement import *
from dotenv import load_dotenv
from cockmachine import cockfight

# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

tracked_message_id = None
tracked_user_name = None

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a simple Telegram bot.")

@bot.message_handler(commands=['random'])
def provide_random(message):
    number = random.randint(1,10)
    bot.reply_to(message,"Fancy random number generator: " + str(number))

@bot.message_handler(commands=['cockfight'])
def cock_fight(message):
    username = message.from_user.username
    global tracked_user_name
    global tracked_message_id
    tracked_user_name = username
    add_player(message.from_user.id,username)
    print("Player added sucessfully " + str(message.from_user.id) + " " + username)
    sent_message = bot.reply_to(message,username + " initiated a big cock fight, Reply to combat 3===D")
    tracked_message_id = sent_message.message_id


@bot.message_handler(commands=['collectedPlayers'])
def print_collected_players(message):
    for player in user_players.items():
        bot.send_message(chat_id=message.chat.id,text=player[2])


@bot.message_handler(func=lambda msg: msg.reply_to_message is not None)
def handle_reply(message):

    if message.reply_to_message.message_id == tracked_message_id:
        second_user_name = message.from_user.username
        bot.reply_to(message, second_user_name + " wants to cockfight " + tracked_user_name)
        bot.send_message(chat_id=message.chat.id,text ="Let's cockfight!")
        add_player(message.from_user.id,second_user_name)
        print("Player added sucessfully " + str(message.from_user.id) + " " + second_user_name)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    number = random.randint(1,2)
    if number == 1:
        bot.reply_to(message, message.text + " Julian leckt keine Eier :)")
    else:
        bot.reply_to(message, message.text + " Julian leckt Eier :)")




bot.polling()
