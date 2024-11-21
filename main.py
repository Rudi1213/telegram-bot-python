import os
import telebot
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a simple Telegram bot.")

@bot.message_handler(commands=['random'])
def provide_random(message):
    number = random.randInt(1,10)
    bot.reply_to(message,"Fancy random number generator: " + number)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text + " Julian leckt keine Eier :)")




bot.polling()
