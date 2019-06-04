# voice.py - Audio output: Text To Speech (TTS)

import logging

import pyttsx3

from oa.core import oa
from oa.modules.abilities.core import get, put


import platform
sys_os = platform.system()
flMac = (sys_os == 'Darwin')
if flMac:
    import subprocess
else:
    import pyttsx3
    import os
    TMP_FILE = "/tmp/tts_temp_sample"


def _in():
    if not flMac:
        tts = pyttsx3.init()
        #voice = tts.getProperty('voices')[26] # the french voice
        #tts.setProperty('voice', 'french+f2')
        #tts.setProperty('rate', 120)
        #tts.runAndWait()

    while not oa.core.finished.is_set():
        s = get()
        logging.debug("Saying: %s", s)

        # Pause Ear (listening) while talking. Mute TTS.
        # TODO: move this somewhere else
        put('speech_recognition', 'mute')

        if flMac:
            _msg = subprocess.Popen(['echo', s], stdout=subprocess.PIPE)
            _tts = subprocess.Popen(['say'], stdin=_msg.stdout)
            _msg.stdout.close()
            _tts.communicate()
        else:
            #tts.say(s)
            #tts.runAndWait()
            os.system("pico2wave -l fr-FR -w {}{} \"{}\"".format(TMP_FILE,".wav", s.lower()))
            os.system("aplay -q {}{}".format(TMP_FILE, ".wav"))

        # Wait until speaking ends.
        # Continue ear (listening). Unmute TTS.
        # TODO: move this somewhere else
        put('speech_recognition', 'unmute')
