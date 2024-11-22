import os
import telebot
import random
from userManagement import *
from dotenv import load_dotenv
from cockmachine import *
from commandconversion import getCommands
# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

tracked_message_id = None
tracked_user_name = None
tracked_user_id = None

special_cock_user_id = None
special_cock_message_id = None
special_cock_number = None
special_cock_guesses = 0

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
    userID = message.from_user.id
    global tracked_user_name
    global tracked_user_id
    global tracked_message_id
    tracked_user_name = username
    tracked_user_id = userID
    add_player(message.from_user.id,username)
    sent_message = bot.reply_to(message,username + " initiated a big cock fight, Reply to combat 3===D")
    tracked_message_id = sent_message.message_id


@bot.message_handler(commands=['collectedPlayers'])
def print_collected_players(message):
    bot.send_message(chat_id=message.chat.id,text = "Trying to print collection")
    for user_id, player in user_players.items():
        name = player.name
        bot.send_message(chat_id=message.chat.id, text=name)

@bot.message_handler(commands=['playerScores'])
def print_player_scores(message):
    playerScores = getAllPlayerScores()
    for name, score in playerScores.items():
        bot.send_message(chat_id=message.chat.id, text=name +" : " + str(score))


@bot.message_handler(func=lambda msg: msg.reply_to_message is not None)
def handle_reply(message):
    if message.reply_to_message.message_id == special_cock_message_id:
        if message.text.isdigit():
            global special_cock_guesses
            if special_cock_guesses > 0:
                special_cock_guesses = special_cock_guesses-1
                sentNumber = int(message.text)
                if sentNumber == special_cock_number:
                    bot.send_message(chat_id=message.chat.id, text="Your cock gets doubled :)")
                    multiplyCock(get_player(message.from_user.id),2)
                else:
                    bot.send_message(chat_id=message.chat.id, text="Time to cut :) :)")
                    divideCock(get_player(message.from_user.id),2)
            else:
                bot.send_message(chat_id=message.chat.id, text="No guesses left for this special cock suprise (Create a new one)")

        else:
            bot.send_message(chat_id=message.chat.id, text="Schreib ma a Zahl du Bastard")

    if message.reply_to_message.message_id == tracked_message_id:
        second_user_name = message.from_user.username
        bot.reply_to(message, second_user_name + " wants to cockfight " + tracked_user_name)
        bot.send_message(chat_id=message.chat.id,text ="Let's cockfight!")
        add_player(message.from_user.id,second_user_name)
        winner = cockfight(get_player(tracked_user_id),get_player(message.from_user.id))
        bot.send_message(chat_id=message.chat.id, text=winner.name + "won the fight")

@bot.message_handler(commands=['specialCockBonus'])
def special_cock_bonus_create(message):
    sent_message = bot.reply_to(message, message.from_user.username + " guess the special cock numberto double your cock")
    global special_cock_user_id
    special_cock_user_id = message.from_user.id
    global special_cock_message_id
    special_cock_message_id = sent_message.message_id
    global special_cock_number
    special_cock_number = random.randint(1,10)
    global special_cock_guesses
    special_cock_guesses= 2
    bot.send_message(chat_id=message.chat.id, text="SPECIAL COCK NUMBER" + str(special_cock_number))
    print("SPECIAL COCK NUMBER" + str(special_cock_number))

@bot.message_handler(commands=['showCommands'])
def show_commands(message):
    commands = getCommands()
    for command, description in commands:
        bot.send_message(chat_id=message.chat.id, text=command + " : " + description)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    number = random.randint(1,2)
    if number == 1:
        bot.reply_to(message, message.text + " Julian leckt keine Eier :)")
    else:
        bot.reply_to(message, message.text + " Julian leckt Eier :)")




bot.polling()
