from telebot import TeleBot
from telebot.types import BotCommand
from commandconversion import getCommands

def register_commands(bot: TeleBot):
    commands_dict = getCommands()
    commands = [BotCommand(cmd, desc) for cmd, desc in commands_dict.items()]
    bot.set_my_commands(commands)


