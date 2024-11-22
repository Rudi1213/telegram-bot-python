from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TOKEN)

commandList = {}
def register_commands(bot: TeleBot):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("hello", "Hello"),
        BotCommand("random", "Randoooom"),
        BotCommand("cockfight","Cockfight"),
        BotCommand("collectedPlayers","Collected players"),
        BotCommand("playerScores", "Player scores"),
        BotCommand("specialCockBonus","Special cock bonus")
    ]


    bot.set_my_commands(commands)

    for command in commands:
        commandList[command.command] = command.description

register_commands(bot)



def get_commands():
    return commandList


