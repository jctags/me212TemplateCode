#!/usr/bin/python

import listening
import talking
import os
import time
import sys
import apriltag_navi

import rospy
import numpy as np
import cv2  # OpenCV module

from sensor_msgs.msg import Image, CameraInfo
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, Pose, Twist, Vector3, Quaternion
from std_msgs.msg import ColorRGBA

from cv_bridge import CvBridge, CvBridgeError
import message_filters
import math

import tf
import threading
import serial
import pdb
import traceback
import tf.transformations as tfm

from pr_apriltags.msg import AprilTagDetections
from me212pillbed.msg import WheelVelCmd
import helper
import math

sys.path.insert(0, '/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/src/me212arm/scripts')
import run_planning
sys.path.insert(0, '/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/src/me212cv/scripts')
print("importing")
import obstacle_detection
print("imported")
time.sleep(3)
wavpath = os.getcwd()+'/Desktop/me212s3/MobileRobot/wav files/'

rospy.init_node('navigation', anonymous=True)
nav = apriltag_navi.ApriltagNavigator()

class Navigator():
	def __init__(self):
		self.listener = tf.TransformListener()
		self.br = tf.TransformBroadcaster()
		self.apriltag_sub = rospy.Subscriber("/apriltags/detections", AprilTagDetections, self.apriltag_callback, queue_size = 1)
		self.velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)   ##

        #rospy.init_node('apriltag_navi', anonymous=True)

        rospy.sleep(1)

	def apriltag_callback(self, data):
		# use apriltag pose detection to find where is the robot
		##
		for detection in data.detections:
			tagframename = '/apriltag' + str(detection.id)
			pose_tag_base = helper.poseTransform(helper.pose2list(detection.pose),  homeFrame = '/camera', targetFrame = '/base_link', listener = self.listener)
			pose_base_map = helper.poseTransform(helper.invPoseList(pose_tag_base), homeFrame = tagframename, targetFrame = '/map', listener = self.listener)
			helper.pubFrame(self.br, pose = pose_base_map, frame_id = '/base_link', parent_frame_id = '/map', npub = 1)

	def path_purple(self):
        # 6 4 3
        wv = WheelVelCmd()
        # straight
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(7)
        # turn to avoid obstacle
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = -0.2
        self.velcmd_pub.publish(wv)
        rospy.sleep(7)
        # reorient
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(2)
        # half circle turn to face shelf
        wv.desiredWV_L = -0.2
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(10)
        # approach shelf
        wv.desiredWV_L = 0.2
        wv.desiredWV_R = 0.2
        self.velcmd_pub.publish(wv)
        rospy.sleep(3)

    def path_notpurple(self):
        # 6 4 3
        wv = WheelVelCmd
        # straight
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(10)
        # turn to avoid obstacle
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = -0.2
        self.velcmd_pub.publish(wv)
        rospy.sleep(7)
        # reorient
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(2)
        # half circle turn to face shelf
        wv.desiredWV_L = -0.1
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(10)
        # approach shelf
        wv.desiredWV_L = 0.2
        wv.desiredWV_R = 0.2
        self.velcmd_pub.publish(wv)
        rospy.sleep(3)

    def target_xbottle(self):
        # 3
        navi_loop([0.5, 2.15, theta])     # target position based on distance from april tag 3

    def bottle_drop(self):
        # 4
        wv = WheelVelCmd
        # backup
        wv.desiredWV_L = -0.3
        wv.desiredWV_R = -0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(3)
        # turn
        wv.desiredWV_L = -0.3
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(5)
        # angled toward drop location
        wv.desiredWV_L = 0.07
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(5)
        # straight to drop location
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = 0.3
        rospy.sleep(3)

    def bedstart(self):
        # 5 7
        wv = WheelVelCmd
        # turn 180
        wv.desiredWV_L = 0.5
        wv.desiredWV_R = 0.5
        self.velcmd_pub.publish(wv)
        rospy.sleep(3)
        # straight to bed start
        wv.desiredWV_L = 0.5
        wv.desiredWV_R = 0.5
        self.velcmd_pub.publish(wv)
        rospy.sleep(5)
        # turn 90 for start position
        wv.desiredWV_L = -0.3
        wv.desiredWV_R = 0.5
        self.velcmd_pub.publish(wv)
        rospy.sleep(3)

    def spread_blanket(self):7
        # 7
        wv = WheelVelCmd()
        wv.desiredWV_L = 0.3
        wv.desiredWV_R = 0.3
        self.velcmd_pub.publish(wv)
        rospy.sleep(10)


nav2 = Navigator()
print("starting purple path")
nav2.path_purple()
print("purple path completed")

# talking.talk(wavpath + 'Anji robot 1 reduced.wav') #which task

# talking.talk(wavpath + 'Anji robot 2 reduced.wav') #which color
# color = listening.listen(['red','green','blue'])
# color = obstacle_detection.whichpath()
# print color
# time.sleep(3)
# talking.talk(wavpath + 'pillbed 3.wav') #navigating!
# # #NAVIGATE (use the color to input to nav)
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

