#!/usr/bin/env python
import os
import rospy            # ROS Python interface
from std_msgs.msg import UInt16MultiArray

class TonePublisher(object):
    
    """
        The following code will make sound on the MiRo
    """
    def __init__(self):
        rospy.init_node("tone_publisher")
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME")
        self.vel_pub = rospy.Publisher(
            topic_base_name + "/control/tone", UInt16MultiArray, queue_size=0
        )

    # linear is to move straight and angular is to turn
    def set_tone(self, data = []):
        tone = UInt16MultiArray()
        tone.data = data
        self.vel_pub.publish(tone)

    def publish(self):
        self.vel_pub.publish(self.tone)

# makes the miro move in circles
tone = TonePublisher()
while not rospy.is_shutdown():
    tone.set_tone(data=[10000, 1000, 100])
