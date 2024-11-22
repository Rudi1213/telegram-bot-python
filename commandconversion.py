from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv

def getCommands():
    commands = [
        BotCommand("hello", "Hello"),
        BotCommand("random", "Funny random gen"),
        BotCommand("cockfight", "Cockfight"),
        BotCommand("collectedPlayers", "Show all collected players"),
        BotCommand("playerScores", "Player scores"),
        BotCommand("specialCockBonus", "Special cock bonus"),
        BotCommand("showCommands", "Shows all available commands"),
        BotCommand("debug", " Debug messages to myself"),
        BotCommand("testGroup", "Test group message")
    ]

    commandsList = {}
    for command in commands:
        commandsList[str(command.command)] = str(command.description)
    return commandsList