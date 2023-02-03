#!/usr/bin/env python
import os
import rospy            # ROS Python interface
from geometry_msgs.msg import TwistStamped

class MovementPublisher(object):
    
    """
        The following code will move the MiRo
    """
    def __init__(self):
        rospy.init_node("movement_publisher")
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME")
        self.vel_pub = rospy.Publisher(
            topic_base_name + "/control/cmd_vel", TwistStamped, queue_size=0
        )

    # linear is to move straight and angular is to turn
    def set_move_cmd(self, linear = 0.0, angular = 0.0):
        vel_cmd = TwistStamped()
        vel_cmd.twist.linear.x = linear
        vel_cmd.twist.angular.z = angular
        self.vel_pub.publish(vel_cmd)

# makes the miro move in circles
movement = MovementPublisher()
while not rospy.is_shutdown():
    movement.set_move_cmd(linear=0.1, angular=0.4)
<<<<<<< HEAD
=======
    movement.publish()
>>>>>>> 2557d55d37e7c3c317aa5c4b013191d592552509
