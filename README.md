## Dynamixel SDK Websockets

This fork of the [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) adds support in python for using a websocket client as a port instead of a serial port. This makes it possible to use WiFi to control your dynamixels. However, it requires the dynamixels to be connected over half-suplex serial to a WiFi-enabledcontrol board (such as an ESP32) that uses a websocket server to relay the comms to and from connected motors. I am developing such a board and will link to it here when it is available.

The Arduino sketch that works as the websocket server is available here:\
https://github.com/nsted/websocketServerForSmartServos

## Usage

To use simply define your port as:\
&nbsp; &nbsp; &nbsp; &nbsp; portHandler = PortHandler("ws://yourServerURL:portnum")\
&nbsp; &nbsp; &nbsp; &nbsp; `portHandler = PortHandler("ws://192.168.1.22:80")`

Send binary with:\
&nbsp; &nbsp; &nbsp; &nbsp; portHandler.writePort([byte1,byte2,...,byteN])

This feature is used by the Dynamixel SDK with calls such as:\
&nbsp; &nbsp; &nbsp; &nbsp; `packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)`

You can also send text with:\
&nbsp; &nbsp; &nbsp; &nbsp; portHandler.writePort("my message here")\
This is useful if you want to handle other commands on the server such as requests for sensor data.

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

- **C**: \*Dynamic library and source code of this library and examples
- **C#** / **Java** / **MATLAB** / **LabVIEW**: Support based on dynamic library using C language
- **C++**: \*Dynamic library and source code of this library and examples
- **Python**: Python module and examples
  (_ Dynamic library (_.dll, _.so, and _.dylib files) / .dll: dynamic-link library on Windows / .so: shared object on Linux / .dylib: dynamic library on MacOS)

For more information on ROS Packages for Dynamixel SDK, please refer to the ROS wiki pages below.

- http://wiki.ros.org/dynamixel_sdk
- http://wiki.ros.org/dynamixel_workbench
- http://wiki.ros.org/dynamixel_workbench_msgs
