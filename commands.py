from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TOKEN)

commands = None

def register_commands(bot: TeleBot):
    global commands
    commands = [
        BotCommand("start", "Hello"),
        BotCommand("hello", "Hello"),
        BotCommand("random", "uuuuh random number"),
        BotCommand("cockfight","Cockfight"),
        BotCommand("collectedPlayers","Show collected players"),
        BotCommand("playerScores", "Show player scores"),
        BotCommand("specialCockBonus","Special cock bonus game"),
        BotCommand("show Commands", "shows all commands"),
    ]
    
    bot.set_my_commands(commands)

def get_commands():
    global commands
    return commands


register_commands(bot)
