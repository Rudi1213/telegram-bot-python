from datetime import datetime
import pytz

def isArbeitslosenGamerHours():
    vienna_tz = pytz.timezone('Europe/Vienna')
    vienna_time = datetime.now(vienna_tz)
    if vienna_time.hour < 14 and vienna_time.weekday() not in [5,6]:
        return True
    else:
        return False

def getViennaTime():
    vienna_tz = pytz.timezone('Europe/Vienna')
    vienna_time = datetime.now(vienna_tz)
    viennaTime = vienna_time.strftime("%H:%M")

    return viennaTime
