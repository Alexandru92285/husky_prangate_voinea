#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    front = msg.ranges[360]
    left = msg.ranges[270]
    right = msg.ranges[450]

    cmd = Twist()

    if front > 1.0:
        cmd.linear.x = 0.5
        cmd.angular.z = 0.0
    else:
        if front < 1.0:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.5
        else:
            if right < 1.0:
                cmd.linear.x = 0.0
                cmd.angular.z = 0.5
            else:
                if left < 1.0:
                    cmd.linear.x = 0.0
                    cmd.angular.z = -0.5

    pub.publish(cmd)

rospy.init_node('evita_pereti')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
