# MiRo Connections

The following content will be looking into how we can connect to the MiRo on-board and off-board(single and multiple MiRos)

## On-board Connection

## Off-board Connection

The following part will act a
### Multiple MiRo Connection

**Step 1:** Set up the MiRo from the MiRo app where the settings are set as follows and then restart:

* Network addressing mode: dynamic
* Network address of ROS master: {ip address of your laptop}
* Robot name: Set it up as your choice where each of the robot should have different names

**Step 2:** Disable Tuos and change 


**Step 1:** Add a launch file where each of the MiRo will be controlled based on its robot name. The<env name="MIRO_ROBOT_NAME" value="miro2"/>
**Step 1:** To do