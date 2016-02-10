# Flight MP3 Examples

ESA have informed us that, due to the operational constraints surrounding approved file types, we are not permitted to upload new Raspbian or Pip packages to the ISS to support the new coding challenges.

This means that, for the MP3 player challenge, entrants must not submit code that depends on non default packages installed via `apt-get` or `pip`. So for example if you did `sudo apt-get install vlc` and then `import vlc` in your Python code this would cause the following error on the Astro Pis in space:

`ImportError: No module named vlc`

Then your program would just end abruptly having done nothing. This happens because the `apt-get` command hasn't been run on the Astro Pis in space and we're unable to upload and install the `vlc` module manually due to issues with approved file types.

To help you we've created two examples of MP3 playback that are **known to work** on the Astro Pis in space which you can adapt and integrate into your own code.

- [Background music function in Pygame](pygame_music.py)
- [Subprocess Omxplayer and send key strokes to control it](omxplayer_shell.py)

So what modules can you use? There are numerous modules built into Python that are known as the *Standard Library*, commonly used modules like `time`, `os`, `math` and `threading` are all part of this. So those modules, and many others, can be used without issue.

The lists below show the Python modules that are installed on the Astro Pis in space.

## Python 2.7

[List of Standard Library modules](https://docs.python.org/2.7/py-modindex.html)

Module | Version
---|---
MySQL-python|1.2.3
Pillow|2.9.0
RPi.GPIO|0.5.11
RTIMULib|7.2.1
argparse|1.2.1
distribute|0.6.24dev-r0
ephem|3.7.5.3
evdev|0.5.0
mcpi|0.1.1
numpy|1.6.2
pep8|1.2
picamera|1.10
pifacecommon|4.1.2
pifacedigitalio|3.0.4
pygame|1.9.1release
pygobject|3.8.2
pyserial|2.5
sense-hat|2.1.0
wsgiref|0.1.2

## Python 3.2

[List of Standard Library modules](https://docs.python.org/3.2/py-modindex.html)

Module | Version
---|---
Pillow|2.9.0
RPi.GPIO|0.5.11
RTIMULib|7.2.1
distribute|0.6.24dev-r0
evdev|0.5.0
mcpi|0.1.1
numpy|1.6.2
picamera|1.10
pifacecommon|4.1.2
pifacedigitalio|3.0.4
pygame|1.9.2a0
pyserial|2.5
sense-hat|2.1.0
spacecraft|0.1.0
wsgiref|0.1.2
