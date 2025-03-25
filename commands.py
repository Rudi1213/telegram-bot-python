from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TOKEN)

def register_commands(bot: TeleBot):
    commands = [
        BotCommand("hello", "Hello"),
        BotCommand("random", "Funny random gen"),
        BotCommand("cockfight","Cockfight"),
        BotCommand("collectedPlayers","Show all collected players"),
        BotCommand("playerScores", "Player scores"),
        BotCommand("specialCockBonus","Special cock bonus"),
        BotCommand("showCommands", "Shows all available commands"),
        BotCommand("debug"," Debug messages to myself"),
        BotCommand("testGroup", "Test group message"),
        BotCommand("gaming", "Gaming time"),
        BotCommand("all", "Tags all users"),
        BotCommand("schuiz", "Schuiz command"),
        BotCommand("gasperl","Gasperl command"),
        BotCommand("kefa", "Kefa command"),
        BotCommand("dahad", "Dahad command"),
    ]


    bot.set_my_commands(commands)



register_commands(bot)




