#!/usr/bin/env python

import os
import rospy    # ROS Python interface
from std_msgs.msg import Int16MultiArray
from tutorial.msg import tutorial
import numpy as np

class MicSubscriber(object):
    
    """
        The following will subscribe to the mic to collect samples for 5 seconds
    """
    def __init__(self):
        rospy.init_node("mic_subscriber")
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME")
        self.subscriber = rospy.Subscriber(topic_base_name + "/sensors/mics", Int16MultiArray, self.callback)
        self.record_data = np.empty(0)
        # publish on a new topic with custom message. The following message includes the sample for 5 seconds with data on the sampling rate.
        self.publisher = rospy.Publisher(
            topic_base_name + "/recording/mic_data", tutorial, queue_size=0
        )
        # calling object for custom message. for more info on the message, use rosmsg info <message_name>.
        self.recording = tutorial()
        self.recording.sampling_rate = 20000
        # to check when message is published
        self.publish_mark = False

    def callback(self, data):
        # record data for 5 seconds or publish if it is more than 5 seconds worth of sample
        if self.record_data < 20000 * 5:
            self.record_data = np.append(self.record_data, data.data)
            self.publish_mark = False
        else:
            self.recording.sampling_data = self.record_data
            # publish the 5 seconds recording
            self.publisher.publish(self.recording)
            self.record_data = np.empty(0)
            self.publish_mark = True
            

microphone = MicSubscriber()
while not rospy.is_shutdown():
    toPrint = "Published? " + microphone.publish_mark 
    print(toPrint)