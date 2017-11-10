# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:48:01 2017

@author: Joseph
"""

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

print("silence please")
with m as source: r.adjust_for_ambient_noise(source)
print('threshold: ', r.energy_threshold)
value = None
while value is None:
    print('listening!')
    with m as source: audio = r.listen(source)
    print('attempting recognition')
    try:
        value = r.recognize_google(audio)
    except:
        print('try again!')

value = value.split()
value = [x.lower() for x in value]
print(value)