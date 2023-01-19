#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def subscriberCallback(msg):
    rospy.loginfo("Received message: %s", msg.data)

if __name__ == '__main__':
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("my_topic", String, subscriberCallback)
    rospy.spin()

