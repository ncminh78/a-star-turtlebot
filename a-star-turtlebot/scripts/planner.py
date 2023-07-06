#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import rospkg


# function to convert file into array
def converter(file):
    for i in range(len(file)):
        file[i] = file[i].split(',')

    return file


# function to run turtlebot3
def runner(order):

    # declaring object for class Twist
    msg = Twist()

    for i in range(len(order)):
        rate = rospy.Rate(2)

        msg.linear.x = float(order[i][0])
        msg.angular.z = float(order[i][1])

        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()


if __name__ == '__main__':

    global pub

    # publisher object publishing to command velocity
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    # initialize node
    rospy.init_node('planner', anonymous=True)

    # read text file


    # convert into array
    orders = converter(orders)
    while True:
        # calling runner
        runner(orders)

    # runnning infinte times
    # rospy.spin()
