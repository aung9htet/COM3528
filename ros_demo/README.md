# Re-Introduction to Programming on Rospy

## Catkin
The cakin contains a set of CMake macros and custom Python scripts to provide extra functionality on top of the normal CMake workflow. These can be used to add the custom messages on top of the standard messages used in ROS such as the `std_msgs` and `geometry_msgs` that may be used for the odometry and as such. These can be done through changes made to two files in it, i.e. the `CMakeLists.txt` and `package.xml`.

### Creating Catkin Package

ROS software is organised into packages that may consist of the code, data, and documentation. Thus, we will start each of the projects in the workspace by creating a new catkin package. This