## Dynamixel SDK Websocket fork
This fork adds support in python for using a websocket client as a port instead of a serial port. This makes it possible to use wifi to control your dynamixels. To use simply define your port as: 

portHandler = PortHandler("ws://yourURL:portnum"),

eg: `portHandler = PortHandler("ws://192.168.1.22:80")`

However, it requires the dynamixels to be connected to a control board (such as an ESP32) that uses a websocket server to relay the comms to and from connected motors. I developed such a board for my own use, so this is a fairly personal project at the moment. If you have such a board, then this may be of use. If there's any interest, then perhaps I can make the board available in some way.

---

[![kinetic-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/kinetic-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/kinetic-devel)
[![melodic-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/melodic-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/melodic-devel)
[![noetic-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/noetic-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/noetic-devel)
[![dashing-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/dashing-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/dashing-devel)
[![foxy-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/foxy-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/foxy-devel)
[![galactic-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/galactic-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/galactic-devel)
[![humble-devel Status](https://github.com/ROBOTIS-GIT/DynamixelSDK/workflows/humble-devel/badge.svg)](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/humble-devel)

<img src="http://emanual.robotis.com/assets/images/sw/sdk/dynamixel_sdk/overview/dynamixel_sdk_concept_logo.jpg">

## Dynamixel SDK
The ROBOTIS Dynamixel SDK is a software development kit that provides Dynamixel control functions using packet communication. The API is designed for Dynamixel actuators and Dynamixel-based platforms. For more information on Dynamixel SDK, please refer to the e-manual below.
- [ROBOTIS e-Manual for Dynamixel SDK](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/)

## Supported Programming Languages
DynamixelSDK supports various programming languages.
- **C**: *Dynamic library and source code of this library and examples
- **C#** / **Java** / **MATLAB** / **LabVIEW**: Support based on dynamic library using C language
- **C++**: *Dynamic library and source code of this library and examples
- **Python**: Python module and examples
(* Dynamic library (*.dll, *.so, and *.dylib files) / .dll: dynamic-link library on Windows / .so: shared object on Linux / .dylib: dynamic library on MacOS)

For more information on ROS Packages for Dynamixel SDK, please refer to the ROS wiki pages below.
- http://wiki.ros.org/dynamixel_sdk
- http://wiki.ros.org/dynamixel_workbench
- http://wiki.ros.org/dynamixel_workbench_msgs
