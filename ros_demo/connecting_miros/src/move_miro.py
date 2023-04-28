#!/usr/bin/env python3
import os
import rospy    # ROS Python interface
from geometry_msgs.msg import TwistStamped  # ROS cmd_vel (velocity control) message

class MoveMiro(object):

    def __init__(self):
        # Individual robot name acts as ROS topic prefix
        rospy.init_node("move_miro")
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME")
        self.vel_pub = rospy.Publisher(
            topic_base_name + "/control/cmd_vel", TwistStamped, queue_size=0
        )
        self.vel_cmd = TwistStamped()

    def set_move_cmd(self, linear = 0.0, angular = 0.0):
        self.vel_cmd.twist.linear.x = linear
        self.vel_cmd.twist.angular.z = angular
        self.vel_pub.publish(self.vel_cmd)

    def stop(self):
        self.set_move_cmd()
        self.vel_pub.publish(self.vel_cmd)

move_miro = MoveMiro()
while not rospy.is_shutdown():
    move_miro.set_move_cmd(linear=0.1)
