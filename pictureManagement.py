import os
import random


def grabAllPics(directory):
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif')  # Add more formats if needed
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(supported_formats)]

def getRandomPic(directory):
    return random.choice(grabAllPics(directory))