#!/usr/bin/env python
import os
import rospy            # ROS Python interface
from sensor_msgs.msg import JointState

class JointPublisher(object):
    
    """
        The following code will move the MiRo
    """
    def __init__(self):
        rospy.init_node("movement_publisher")
        self.position = None
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME")
        self.joint_pub = rospy.Publisher(
            topic_base_name + "/control/kinematic_joints", JointState, queue_size=0
        )

    # movement for either tilt, lift, yaw or pitch
    def set_move_joint(self, tilt = 0, lift = 0, yaw = 0, pitch = 0):
        self.joint_cmd = JointState()
        self.joint_cmd.position = [tilt, lift, yaw, pitch]

    # publish message
    def publish(self):
        self.joint_pub.publish(self.joint_cmd)

movement = JointPublisher()
while not rospy.is_shutdown():
    movement.set_move_joint()
    movement.publish()
