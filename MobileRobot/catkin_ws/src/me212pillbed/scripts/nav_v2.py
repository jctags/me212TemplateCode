#!/usr/bin/python

# F2017 2.12 Section 3 navigation

import apriltag_navi
import math

#navi = ApriltagNavigator()
# input = [x,y,th]
# x,y in meters
# th in radians

def path_purple(self):
    # 6 4 3

    navigate([0.3, 1.1, 0])
    navigate([1.02,1.1, math.pi/4])
    navigate([1.02, 2.15, 0])
    navigate([0.56, 2.15, -math.pi/4])

def path_notpurple(self):
    # 6 4 3
    navigate([0.3, 1.64, 0])
    navigate([1.02,1.64, math.pi/4])
    navigate([1.02, 2.15, 0])
    navigate([0.56, 2.15, -math.pi/4])

def target_xbottle(self):
    # 3
    navi_loop([0.5, 2.15, theta])     # target position based on distance from april tag 3

def bottle_drop(self):
    # 4
    navigate([1.62, 1.6, -7*math.pi/6])
    navigate([2.12, 1.6, -math.pi/4])

def bedstart(self):
    # 5 7
    navigate([1.75, 2, -math.pi])
    navigate([1.38, 1.6, -math.pi])

def spread_blanket(self):7
    # 7
    wv = WheelVelCmd()
    wv.desiredWV_R = 0.5
    wv.desiredWV_L = 0.5
    self.velcmd_pub.publish(wv)
    rospy.sleep(1)
