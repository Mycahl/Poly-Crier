#! /usr/bin/env python


import rospy
from std_msgs.msg import String 
from random import randint
def chatter(): 
	names = ["Dr. Bushey", "Vamsi", "Jon"] 
	rospy.init_node('chatter') 
	pub = rospy.Publisher('names', String)
	rate = rospy.Rate(21)

	while not rospy.is_shutdown():
		number = randint(0,2)
		pub.publish(names[number])
		rate.sleep()

if __name__ == '__main__':
	try:
		chatter()
	except rospy.ROSInterruptException:
		pass
