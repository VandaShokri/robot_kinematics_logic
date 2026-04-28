# Robot Kinematics Logic

This ROS 2 package contains the kinematics node for joint state calculations.

## Overview
- **Node Name:** `kinematics_node`
- **Topic:** `/joint_angles`
- **Data Type:** `Float64MultiArray` (3 joints)

## Current Implementation
The node currently publishes **dynamic placeholder values** using a sine wave based on the system clock. This allows for:
1. Verification of the communication middleware (DDS).
2. Visual testing of joint movement in simulators like RViz.
3. Confirmation of the 1Hz publishing frequency.

## How to Build and Run
From the root of the workspace:
```bash
colcon build --packages-select robot_logic
source install/setup.bash
ros2 run robot_logic kinematics_node
