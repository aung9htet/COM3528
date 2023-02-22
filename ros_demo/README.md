# Re-Introduction to Programming on Rospy

The following tutorial should give a revision on how to produce a new package based on catkin and how you can use this catkin packages for development. As an example for the tutorial, we will be working on creating a package which would consist of creating 3 nodes. One will be set on recording and processing the sampling data from the microphone. The processed data from this will then be published which will be used by another node for producing the sound on the MiRo, as well as to save them.

## Catkin
The cakin contains a set of CMake macros and custom Python scripts to provide extra functionality on top of the normal CMake workflow. These can be used to add the custom messages on top of the standard messages used in ROS such as the `std_msgs` and `geometry_msgs` that may be used for the odometry and as such. These can be done through changes made to two files in it, i.e. the `CMakeLists.txt` and `package.xml`.

### Creating Catkin Package

ROS software is organised into packages that may consist of the code, data, and documentation. Thus, we will start each of the projects in the workspace by creating a new catkin package. The catkin packages created in the following format:
```
catkin_create_pkg <package_name> <dependecy1> <dependecy2> <dependency3> ..
```
In the following example, the tutorial is dependent on `std_msgs` and `rospy` and thus is produced as follows:
```
catkin_create_pkg tutorial std_msgs rospy
```

### Creating ROS messages

For creating messages, we would first create a directory in the tutorial named `msg`. In this directory, we would be creating a file for the messages, i.e. `tutorial.msg` in this case. This file would contain instructions on how the message would be defined, which can be seen in example. This would then be followed by adding dependencies to the packages for message generation. Thus, we would start by first adding the following lines to `package.xml`:
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
We would then be editing `CMakeLists.txt` to include the following set of codes depending on the requirements:
```
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
```
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```
```
add_message_files(
  FILES
  <message1.msg>
  <message2.msg>
  <message3.msg>
  ...
)
```

The following steps would allow their own message in the workspace. To use the messages set in the workspace, we would direct ourselves to the base of the workspace for cleaning and rebuilding the workspace. This can be done as follow:
```
cd ~/catkin_ws/
catkin clean
catkin build
source devel/setup.bash
```
To check if the message has been generated, we can use the following command:
```
rosmsg list
```
In the list, you could check if it has successfully generated the message you desire, in this case it would be `tutorial/tutorial`.