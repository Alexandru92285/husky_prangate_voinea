cmake_minimum_required(VERSION 3.0.2)
project(ardrone_action)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  actionlib
  actionlib_msgs
)

add_action_files(
  DIRECTORY action
  FILES DroneControl.action
)

generate_messages(
  DEPENDENCIES actionlib_msgs std_msgs
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs std_msgs rospy
)
