import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+XXDDD9XXXXXXXX','+XXDDD9XXXXXXXX']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[1],'VAMOS AUTOMATIZAR TUDO!',datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')