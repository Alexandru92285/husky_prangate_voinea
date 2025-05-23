#!/usr/bin/env python

import rospy
import actionlib
from ardrone_action.msg import DroneControlAction, DroneControlFeedback, DroneControlResult

class DroneActionServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer(
            'drone_control',
            DroneControlAction,
            self.execute,
            False
        )
        self.feedback = DroneControlFeedback()
        self.result = DroneControlResult()
        self.current_action = ""
        self.server.start()

    def execute(self, goal):
        rate = rospy.Rate(1)
        if goal.command == "TAKEOFF":
            rospy.loginfo("Drone takeoff")
            self.current_action = "TAKING OFF"
        elif goal.command == "LAND":
            rospy.loginfo("Drone land")
            self.current_action = "LANDING"
        else:
            rospy.loginfo("Comanda gresita")
            self.result.success = False
            self.server.set_aborted(self.result)
            return

        while not self.server.is_preempt_requested():
            self.feedback.current_action = self.current_action
            self.server.publish_feedback(self.feedback)
            rate.sleep()

        self.result.success = True
        self.server.set_succeeded(self.result)

if __name__ == "__main__":
    rospy.init_node("drone_action_server")
    DroneActionServer()
    rospy.spin()
