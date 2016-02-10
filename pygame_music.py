#!/usr/bin/python
import time
import os
import pygame.mixer

# Set audio output to Analogue Jack
os.system("sudo amixer cset numid=3 1")
# Set system volume to 100% then control using pygame
os.system("sudo amixer cset numid=1 100%")

pygame.mixer.init()

# See http://www.pygame.org/docs/ref/music.html
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

for i in reversed(range(1, 11)):  # Pan volume down
    pygame.mixer.music.set_volume(i / 10.0)
    time.sleep(1)

for i in range(1, 11):  # Pan volume up
    pygame.mixer.music.set_volume(i / 10.0)
    time.sleep(1)

pygame.mixer.music.pause()  # Pause music for 2 seconds
time.sleep(2)
pygame.mixer.music.unpause()

while pygame.mixer.music.get_busy():  # Wait for mp3 to finish
    time.sleep(0.1)
