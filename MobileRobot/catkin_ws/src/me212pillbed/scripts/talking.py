# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:39:02 2017

@author: Joseph
"""

import pyaudio
import wave

CHUNK = 1024
def talk(filename):

    wf = wave.open(filename, 'rb')
    
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    
    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    # read data
    data = wf.readframes(CHUNK)
    
    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    # stop stream (4)
    stream.stop_stream()
    stream.close()
    
    # close PyAudio (5)
    p.terminate()
    
#note well: code does not proceed until audio is complete