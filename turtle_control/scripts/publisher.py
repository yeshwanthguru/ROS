#!/usr/bin/env python3.8
import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('publisher', anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

while True:
    msg = Twist()
    # Set the linear and angular velocity values
    msg.linear.x = 1.0
    msg.angular.z = 0.5
    # Publish the velocity command
    pub.publish(msg)
    time.sleep(1)

