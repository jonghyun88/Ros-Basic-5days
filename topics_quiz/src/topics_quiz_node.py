#! /usr/bin/env python 
# This line will ensure the interpreter used is the first one on your environment's $PATH. Every Python file needs
# to start with this line at the top.

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import atexit


def callback(msg):
    
    # print(msg.ranges)
    move = Twist()

    if (msg.ranges[180] < 0.5 or msg.ranges[200] < 0.5 or msg.ranges[160] < 0.5): # if robot place obstacle distance under 1m, turn right or turn left 
        print("turn")
            
        if (msg.ranges[225] <= msg.ranges[135]):
            print("left")
            move.linear.x = 0
            move.angular.z = -0 #Move the with an angular velocity in the z axis


        else:
            print("Right")
            move.linear.x = 0
            move.angular.z = 0 #Move the with an angular velocity in the z axis

    else:
        move.linear.x = 0
        print("go")

    pub.publish(move)


rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
