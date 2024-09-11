import keyboard
import uuid #ekrandan kayıt almak icin
import time
import os
from PIL import Image
from mss import mss
"""
https://www.trex-game.skipser.com/
"""

mon = {"top" : 476,
       "left": 641,
       "width":280,
       "height":120}
sct = mss()#ekrandan belirledigimiz alanı kesip frame haline donusturucek
i = 0
file_name = "img"
os.makedirs(file_name,exist_ok=True)
def record_screnn (record_id,key):
    global i
    i+=1
    print("{}  {} ".format(key,id))
    img = sct.grab(mon)
    im = Image.frombytes("RGB",img.size,img.rgb)
    im.save("./img/{}_{}_{}.png".format(key,record_id,i))

is_Exit = False

def exit():
    global is_Exit
    is_Exit = True
    
keyboard.add_hotkey("esc",exit)

record_id = uuid.uuid4()

while True:

    if is_Exit: break
    
    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screnn(record_id, "up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screnn(record_id, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):#devam et
            record_screnn(record_id, "right")
            time.sleep(0.1)
    except RuntimeError: continue

