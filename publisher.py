#!/usr/bin/env python3.8
import rospy
from std_msgs.msg import String
import time

rospy.init_node('publisher', anonymous=True)
pub = rospy.Publisher('my_topic', String, queue_size=10)

while not rospy.is_shutdown():
    msg = String()
    msg.data = "qrobot says hi"
    pub.publish(msg)
    time.sleep(1)

