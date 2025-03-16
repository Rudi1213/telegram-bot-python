import os
from datetime import datetime
import pytz
import telebot
from dotenv import load_dotenv

import userManagement
from cockmachine import *
from commandconversion import getCommands
from patchnotes import patchnotes
from mediaManagement import *
from userManagement import *
patchnotes_sent = 0
from timeManagement import *


# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
admin_chat = os.getenv('MY_CHAT_ID')
group_chat = os.getenv('GROUP_CHAT_ID')
bot = telebot.TeleBot(TOKEN)

tracked_message_id = None
tracked_user_name = None
tracked_user_id = None

special_cock_user_id = None
special_cock_message_id = None
special_cock_number = None



@bot.message_handler(commands=['hello'])
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
    player = get_player(message.from_user.id)
    sent_message = bot.reply_to(message,username + " initiated a big cock fight, Reply to combat 3===D")
    tracked_message_id = sent_message.message_id
    add_cockfight(player,tracked_message_id)


@bot.message_handler(commands=['collectedPlayers'])
def print_collected_players(message):
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
    game = get_specialcock(message.reply_to_message.message_id)
    if game is not None and game.gameType == GameType.SPECIAL:
        if message.text.isdigit():
            if game.guesses > 0:
                player = get_player(message.from_user.id)
                game.guesses = game.guesses-1
                sentNumber = int(message.text)
                if sentNumber == special_cock_number:
                    bot.send_message(chat_id=message.chat.id, text="Your cock gets doubled :)")
                    multiplyCock(player,2)
                    bot.send_message(chat_id=message.chat.id, text="Your new length: " + str(player.score))
                    remove_specialcock(game.messageID)

                else:
                    bot.send_message(chat_id=message.chat.id, text="Time to cut :) :)")
                    divideCock(player,2)
                    bot.send_message(chat_id=message.chat.id, text="Your new length: " + str(player.score))
                    if game.guesses == 0:
                        remove_specialcock(game.messageID)


            else:
                bot.send_message(chat_id=message.chat.id, text="No guesses left for this special cock suprise (Create a new one)")
                remove_specialcock(game.messageID)

        else:
            bot.send_message(chat_id=message.chat.id, text="Schreib ma a Zahl du Bastard")
    elif get_cockfight(message.reply_to_message.message_id) is not None:
        game = get_cockfight(message.reply_to_message.message_id)
        if game.gameType == GameType.COCKFIGHT:
            second_user_name = message.from_user.username
            player1 = get_player(game.player.user_id)
            player2 = get_player(message.from_user.id)
            if player1.user_id == player2.user_id:
                bot.send_message(chat_id=message.chat.id, text="You can't cockfight yourself")
            else:
                bot.reply_to(message, second_user_name + " wants to cockfight " + player1.name)
                add_player(message.from_user.id,second_user_name)
                winner = cockfight(player1,player2)
                bot.send_message(chat_id=message.chat.id, text=winner.name + " won the fight")
                bot.send_message(chat_id=message.chat.id, text="New cock sizes\n" + player1.name + ": " + str(player1.score) +"\n" + player2.name +": " + str(player2.score))
                remove_cockfight(game.messageID)


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
    player = get_player(message.from_user.id)
    tracked_message_id = sent_message.message_id
    add_specialcock(player, tracked_message_id)
    bot.send_message(chat_id=admin_chat, text=str(special_cock_number))


@bot.message_handler(commands=['showCommands'])
def show_commands(message):
    add_player(message.from_user.id, message.from_user.username)
    commands = getCommands()
    commandMessage = " "
    for command, description in commands.items():
        commandMessage = commandMessage + "/" + command+ " : " + description + "\n"

    bot.send_message(chat_id=message.chat.id, text=commandMessage)

######################## DEBUG ########################################
@bot.message_handler(commands=['debug'])
def debugMessager(message):
    bot.send_message(chat_id=admin_chat, text=message.chat.id)

@bot.message_handler(commands=['save'])
def savePlayers(message):
    userManagement.save_players()
    bot.send_message(chat_id=admin_chat, text="Players saved successfully")

@bot.message_handler(commands=['testGroup'])
def asyncGroupMessage(message):
    bot.send_message(chat_id=group_chat, text="Test asynchronous grp message")

@bot.message_handler(commands=['gaming'])
def gaming(message):
    if isArbeitslosenGamerHours():
        Zeit = getViennaTime()
        bot.reply_to(message, "Es is grodmoi " + Zeit + " suach da a Hokn")
    else:
        users = getAllUsers()
        groupMessage = ""
        for user in users:
            groupMessage = groupMessage + user + "\n"

        groupMessage = groupMessage + "It's gaming time jimbos"
        bot.send_message(chat_id=message.chat.id, text=groupMessage)

@bot.message_handler(commands=['gasperl','schuiz','kefa','dahad','thot'])
def sendMedia(message):
    command = message.text
    extractedCommand = "media"+command
    directory = extractedCommand.split('@')[0]
    random_Media = getRandomMedia(directory)

    for pic_format in picture_formats:
        if pic_format in random_Media.lower():
            with open(random_Media, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                return

    for video_format in video_formats:
        if video_format in random_Media.lower():
            with open(random_Media, "rb") as video:
                bot.send_video(message.chat.id, video)
                return






@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    add_player(message.from_user.id, message.from_user.username)
    number = random.randint(1,2)
    if number == 1:
        bot.reply_to(message, message.text + " Julian leckt keine Eier :)")
    else:
        bot.reply_to(message, message.text + " Julian leckt Eier :)")





def manualDebug(debugMessage):
    bot.send_message(chat_id=debugMessage.chat.id, text=debugMessage.text)

def send_patch_notes():
    if patchnotes != "":
        bot.send_message(chat_id=group_chat, text=patchnotes)



if patchnotes_sent == 0:
    send_patch_notes()
    patchnotes_sent = 1


bot.polling()
