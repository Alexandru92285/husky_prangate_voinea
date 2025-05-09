#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from square_service_pkg.srv import SquareMovement, SquareMovementResponse
import math

def move_in_square(side_length, repetitions):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    move = Twist()
    rate = rospy.Rate(10)

    for _ in range(repetitions):
        for _ in range(4):
            
            move.linear.x = 0.2
            move.angular.z = 0.0
            t0 = rospy.Time.now().to_sec()
            while rospy.Time.now().to_sec() - t0 < side_length / 0.2:
                pub.publish(move)
                rate.sleep()


            move.linear.x = 0.0
            pub.publish(move)
            rospy.sleep(1)


            move.angular.z = 0.5
            t0 = rospy.Time.now().to_sec()
            while rospy.Time.now().to_sec() - t0 < (math.pi / 2) / 0.5:
                pub.publish(move)
                rate.sleep()


            move.angular.z = 0.0
            pub.publish(move)
            rospy.sleep(1)

    return True

def handle_square_request(req):
    success = move_in_square(req.side, req.repetitions)
    return SquareMovementResponse(success)

def square_service_server():
    rospy.init_node('square_service_server')
    service = rospy.Service('/square_move', SquareMovement, handle_square_request)
    rospy.loginfo("Service ready to receive square move commands.")
    rospy.spin()

if _name_ == "_main_":
    square_service_server()
