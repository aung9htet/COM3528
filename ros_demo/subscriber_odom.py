#!/usr/bin/env python
import os
import rospy    # ROS Python interface
from nav_msgs.msg import Odometry   # ROS odometry subsciriber
from tf.transformations import euler_from_quaternion

class OdomSubscriber(object):
    
    """
        The following code will provide information on the estimated odometry data of the MiRo
    """
    def __init__(self):
        rospy.init_node("odom_subscriber")
        self.x = 0
        self.y = 0
        self.yaw = 0
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME")
        self.subscriber = rospy.Subscriber(topic_base_name + "/sensors/odom", Odometry, self.callback)

    def callback(self, data):
        orientation = data.pose.pose.orientation
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y
        (_, _, self.yaw) = euler_from_quaternion([orientation.x,
            orientation.y, orientation.z, orientation.w],'sxyz')

odom = OdomSubscriber()
while not rospy.is_shutdown():
    toPrint = "position x: " + str(odom.x) + "\nposition y: " + str(odom.y) + "\ntheta: " + str(odom.yaw)
    print(toPrint)
    rospy.sleep(0.5)    # to slow down the printing