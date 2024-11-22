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
    lul = random.randint(1,100)
    if lul != 52:
        bot.reply_to(message, "Hello! I'm a simple Telegram bot.")
    else:
        bot.reply_to(message, "Hurensohn")


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
    bot.send_message(chat_id=message.chat.id, text=str(message.chat.id))
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
                player = get_player(message.from_user.id)
                special_cock_guesses = special_cock_guesses-1
                sentNumber = int(message.text)
                if sentNumber == special_cock_number:
                    bot.send_message(chat_id=message.chat.id, text="Your cock gets doubled :)")
                    multiplyCock(player,2)
                    bot.send_message(chat_id=message.chat.id, text="Your new length: " + str(player.score))

                else:
                    bot.send_message(chat_id=message.chat.id, text="Time to cut :) :)")
                    divideCock(player,2)
                    bot.send_message(chat_id=message.chat.id, text="Your new length: " + str(player.score))

            else:
                bot.send_message(chat_id=message.chat.id, text="No guesses left for this special cock suprise (Create a new one)")

        else:
            bot.send_message(chat_id=message.chat.id, text="Schreib ma a Zahl du Bastard")

    if message.reply_to_message.message_id == tracked_message_id:
        second_user_name = message.from_user.username
        bot.reply_to(message, second_user_name + " wants to cockfight " + tracked_user_name)
        add_player(message.from_user.id,second_user_name)
        player1 = get_player(tracked_user_id)
        player2 = get_player(message.from_user.id)
        if player1.user_id == player2.user_id:
            bot.send_message(chat_id=message.chat.id, text="You can't cockfight yourself")
        else:
            winner = cockfight(get_player(tracked_user_id),get_player(message.from_user.id))
            bot.send_message(chat_id=message.chat.id, text=winner.name + " won the fight")
            bot.send_message(chat_id=message.chat.id, text="New cock sizes\n" + player1.name + ": " + str(player1.score) +"\n" + player2.name +": " + str(player2.score))

@bot.message_handler(commands=['specialCockBonus'])
def special_cock_bonus_create(message):
    add_player(message.from_user.id, message.from_user.username)
    sent_message = bot.reply_to(message, message.from_user.username + " guess the special cock number to double your cock (reply to this message) (special cock number is always between 1-10)")
    global special_cock_user_id
    special_cock_user_id = message.from_user.id
    global special_cock_message_id
    special_cock_message_id = sent_message.message_id
    global special_cock_number
    special_cock_number = random.randint(1,10)
    global special_cock_guesses
    special_cock_guesses= 2
    print("SPECIAL COCK NUMBER" + str(special_cock_number))

@bot.message_handler(commands=['showCommands'])
def show_commands(message):
    add_player(message.from_user.id, message.from_user.username)
    commands = getCommands()
    for command, description in commands.items():
        bot.send_message(chat_id=message.chat.id, text="/"+command + " : " + description)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    add_player(message.from_user.id, message.from_user.username)
    number = random.randint(1,2)
    if number == 1:
        bot.reply_to(message, message.text + " Julian leckt keine Eier :)")
    else:
        bot.reply_to(message, message.text + " Julian leckt Eier :)")


def debug(debugMessage):
    bot.send_message(chat_id=debugMessage.chat.id, text=debugMessage.text)


bot.polling()
