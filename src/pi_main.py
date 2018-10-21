
#!usr/bin/env python

import rospy
from std_msgs.msg import UInt8

def navigation_callback(data):
    print(data)

rospy.init_node('Pi_Node')
rospy.Subscriber('navigation',UInt8,navigation_callback)
rospy.spin()