#! /usr/bin/env python


import rospy
from std_msgs.msg import String 

def callback(x): 
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", x.data)

def listener():
	rospy.init_node('poly_listener')
	sub = rospy.Subscriber('names', String, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass

