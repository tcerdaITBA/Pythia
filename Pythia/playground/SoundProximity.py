import os
import serial
import random
import time

from pygame import mixer

mixer.init()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 5) # 5 secs timeout
songs = []

for filename in os.listdir('./music'):
    if '.mp3' in filename:
        songs.append('music/' + filename)

print songs

mixer.music.load(songs[0])
mixer.music.play()

while True:
    state = ser.readline().strip()
    select = -1

    if 'isNear' in state:
        select = random.randint(0, len(songs)-1)

        print 'playing: ', songs[select]

        mixer.music.load(songs[select])
        mixer.music.set_volume(1)
        mixer.music.play()

    elif 'talking' in state:
        mixer.music.set_volume(0.2)

    elif 'silence' in state:
        mixer.music.set_volume(1)

    print state

