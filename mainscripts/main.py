#!/usr/bin/python

Isoff = True
Isdrawer = False
Istowel = False
Isblanket = False
Ispills = False
#These are the strings outputted by the listener.py
#AudioTrans
#AudioTask
#AudioPillColor

while Isoff:
	OnAudioTrans = str(input("type here \n"))##listener.output()#call listener.py and get the string that it outputs
	if (OnAudioTrans == "start"): #could change to "Hello" or whatever
		Isoff = False

#Somehow have the robot ask which task it can do today
#create a loop here in case it hears something wrong

if(not Isoff):
	AudioTask = str(input("type here")) ##listener.ouput()
	if (AudioTask == "drawer"):
		Isdrawer = True
	if (AudioTask == "towel"):
		Istowel = True
	if (AudioTask == "blanket"):
		Isblanket = True
	if (AudioTask == "pills"):
		Ispills = True
	#we can have a line that turns the camera on here if we want...
	

if Ispills:
	#Somehow have the robot ask which color pill bottle color
	AudioPillColor = listener.output() #green,yellow, whatever
	
	
	#compile list of keywords audio
