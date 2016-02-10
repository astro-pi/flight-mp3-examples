#!/usr/bin/python
import time
import os
import subprocess


"""
omxplayer keys

1           decrease speed
2           increase speed
<           rewind
>           fast forward
z           show info
j           previous audio stream
k           next audio stream
i           previous chapter
o           next chapter
n           previous subtitle stream
m           next subtitle stream
s           toggle subtitles
w           show subtitles
x           hide subtitles
d           decrease subtitle delay (- 250 ms)
f           increase subtitle delay (+ 250 ms)
q           exit omxplayer
p / space   pause/resume
-           decrease volume
+ / =       increase volume
left arrow  seek -30 seconds
right arrow seek +30 seconds
down arrow  seek -600 seconds
up arrow    seek +600 seconds
"""


# Set audio output to Analogue Jack
os.system("sudo amixer cset numid=3 1")
# Set system volume to 100% then control using omxplayer
os.system("sudo amixer cset numid=1 100%")


def send_key_press(key):
    global proc
    proc.stdin.write(key.encode('utf-8'))
    proc.stdin.flush()

file = "test.mp3"

proc = subprocess.Popen(["omxplayer", file, "-o", "local", "-I"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    close_fds=True)

for i in range(5):
    send_key_press('-')  # Pan volume down
    time.sleep(1)

for i in range(5):
    send_key_press('+')  # Pan volume up
    time.sleep(1)

send_key_press('p')  # Pause music for 2 seconds
time.sleep(2)
send_key_press('p')

while proc.poll() is None:  # Wait for mp3 to finish
    time.sleep(0.1)
