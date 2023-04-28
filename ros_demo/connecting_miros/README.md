# MiRo Connections

The following content will be looking into how we can connect to the MiRo on-board and off-board(single and multiple MiRos)

## On-board Connection

**Step 1** Connect to the same network.

**Step 2** Type in ```ssh miro@<robot_ip_address>```. Type ```yes``` and the password is ```miro```.

In here, you can transfer files from your local pc directory to the MiRo's local directory as follows: ```scp <local_file> miro@<robot_ip_address>:<robot_local_file>```
## Off-board Connection

### Single MiRo Connection

This could be done through implementation of the tuos as shown in previous labs.

### Multiple MiRo Connection

**Step 1:** Set up the MiRo from the MiRo app where the settings are set as follows and then restart:

* Network addressing mode: dynamic
* Network address of ROS master: {ip address of your laptop}
    * The ip address of your laptop can be obtained through the use of ```ifcongif```. It should be part of the net-tools package.
* Robot name: Set it up as your choice where each of the robot should have different names

**Step 2:** Type in ```nano ~/.bashrc``` and add in the line ```source ~/mdk/setup.bash```. Comment out executing for the tuos.

**Step 3** Open the file for the user setup, which could be seen in the configuration at the start of a new tab/executing the miro mdk. In the bash script, change the following:
* MIRO_NETWORK_MODE = dynamic
* ROS_MASTER_IP = {ip address of your laptop}

**Step 4** Add a launch file in a folder called ```launch/``` where each of the MiRo will be controlled based on its robot name. A sample can be seen in ```multiple_miro.launch``` where it have used ```<env name="MIRO_ROBOT_NAME" value="miro2"/>``` to change the environemnt name.

**Step 5** Add the following lines to ```package.xml```:
* ```<build_depend>roslaunch</build_depend>```
* ```<build_export_depend>roslaunch</build_export_depend>```
* ```<exec_depend>roslaunch</exec_depend>```

**Step 6** In ```CMakeLists.txt```, add the following compenent ```roslaunch``` to the list of packages to be used as follows: ``` find_package(catkin REQUIRED COMPONENTS roslaunch <package_1> <package_2> ...)```. Add the following line as well to the file ```roslaunch_add_file_check(launch)```.

**Step 7:**  Rebuild the catkin package by using ```catkin clean``` and ```catkin build``` in ```~/mdk/catkin_ws/```. Then re-source the workspace using ```source ~/mdk/catkin_ws/devel/setup.bash```. This will allow you to find and run the roslaunch file as follows: ```roslaunch <project_name> <launch_file>```. An example of the launch files and edits made to the ```package.xml``` and ```CMakeLists.txt``` can be seen in this sample tutorial.