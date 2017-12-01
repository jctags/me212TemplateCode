#!/usr/bin/python

import listening
import talking
import os
import time
import sys
sys.path.insert(0, '/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/src/me212arm/scripts')
import run_planning
sys.path.insert(0, '/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/src/me212cv/scripts')
print("importing")
import obstacle_detection
print("imported")
time.sleep(3)
wavpath = os.getcwd()+'/Desktop/me212s3/MobileRobot/wav files/'

# talking.talk(wavpath + 'Anji robot 1 reduced.wav') #which task

# talking.talk(wavpath + 'Anji robot 2 reduced.wav') #which color
# color = listening.listen(['red','green','blue'])
#time.sleep(3)
# talking.talk(wavpath + 'pillbed 3.wav') #navigating!
# # #NAVIGATE
# run_planning.grip_change("close")
# print("print1")
# talking.talk(wavpath + 'pillbed 4.wav') #approaching you
# # #NAVIGATE
# talking.talk(wavpath + 'pillbed 5.wav') # open the bottle and say release
# listening.listen(['release'])
# run_planning.grip_change("open")
# talking.talk(wavpath + 'pillbed 6.wav') #anything else I can help you with?
# time.sleep(3)
# talking.talk(wavpath + 'pillbed 7.wav') #place blanket in my gripper
# listening.listen(['close'])
# run_planning.grip_change("close")
# # #NAVIGATE
# talking.talk(wavpath + 'pillbed 8.wav') # say begin when ready
# listening.listen(['begin'])
# # #NAVIGATE
# talking.talk(wavpath + 'pillbed 9.wav') #say done to release
# listening.listen(['done'])
# run_planning.grip_change("open")
obstacle_detection.main()
ready = False
while(not ready):
	print("entered loop")
	if(obstacle_detection.isPurpleReady()):
		#execute purple navigating
		ready = True
		print("I will navigate purple")
	elif(obstacle_detection.isGreenReady()):
		#execute green navigating
		ready = True
		print("I will navigate green")
	else:
		print("None are ready")