%2.12 Section 3 - Task B
% gripper close script

import rospy
import std_msgs.msg, sensor_msgs.msg
import numpy as np

rospy.init_node("close_gripper")

exec_joint1_pub = rospy.Publisher('/joint1_controller/command', std_msgs.msg.Float64, queue_size=1)

exec_joint1_pub.publish(std_msgs.msg.Float64(0))
