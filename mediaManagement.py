import os
import random

picture_formats = ('.jpg', '.jpeg', '.png')
video_formats = ('.mp4', '.mov', '.avi', '.m4v', '.wmv', '.gif')
all_formats = picture_formats + video_formats

def grabAllPics(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(picture_formats)]

def getRandomPic(directory):
    return random.choice(grabAllPics(directory))


def grabAllGIFs(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp4')]

def getRandomGIF(directory):
    return random.choice(grabAllGIFs(directory))

def grabAllMedia(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(all_formats)]

def getRandomMedia(directory):
    return random.choice(grabAllMedia(directory))