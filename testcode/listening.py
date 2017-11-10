# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:48:01 2017

@author: Joseph
"""

import speech_recognition as sr

def listen(keywords):
    '''
    Takes in a list of keywords as lowercase individual words 
    Listens until it hears one of those keywords, then returns the word
    '''
    r = sr.Recognizer()
    m = sr.Microphone()
    r.energy_threshold = 2000
    while True:
        value = None
        while value is None:
            with m as source: audio = r.listen(source)
            try:
                value = r.recognize_google(audio)
                value = value.split()
                value = [x.lower() for x in value]
            except:
                pass
        for word in value:
            if word in keywords:
                return word
