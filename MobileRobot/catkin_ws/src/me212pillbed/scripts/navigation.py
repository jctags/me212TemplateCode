#!/usr/bin/python

import listening
import talking
import os
import time

wavpath = os.getcwd()+'/Desktop/me212s3/MobileRobot/wav files/'

talking.talk(wavpath + 'Anji robot 1.wav') #which task
time.sleep(3)
talking.talk(wavpath + 'Anji robot 2.wav') #which color
color = listening.listen(['red','green','blue'])
talking.talk(wavpath + 'pillbed 3.wav') #navigating!
#NAVIGATE
#CLOSE GRIPPER
talking.talk(wavpath + 'pillbed 4.wav') #approaching you
#NAVIGATE
talking.talk(wavpath + 'pillbed 5.wav') # open the bottle and say release
listening.listen(['release'])
#OPEN GRIPPER
talking.talk(wavpath + 'pillbed 6.wav') #anything else I can help you with?
time.sleep(3)
talking.talk(wavpath + 'pillbed 7.wav') #place blanket in my gripper
listening.listen(['close'])
#CLOSE GRIPPER
#NAVIGATE
talking.talk(wavpath + 'pillbed 8.wav') # say begin when ready
listening.listen(['begin'])
#NAVIGATE
talking.talk(wavpath + 'pillbed 9.wav') #say done to release
listening.listen(['release'])
# CLOSE GRIPPER