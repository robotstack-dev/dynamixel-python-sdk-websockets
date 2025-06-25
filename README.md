# dynamixelSDK_websockets

This is a fork of the [official Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) that adds WebSocket support, enabling wireless control of Dynamixel servos.

## WebSocket Support

This fork adds support for using a WebSocket client as a port in place of a serial port. This makes it possible to wirelessly control your robot!

It requires the servos to be connected over half-duplex serial to a WiFi-enabled microcontroller (e.g. ESP32) that uses a WebSocket server to relay the comms to and from connected motors. The **[RobotStack Smart Servo Add-On Board](https://www.tindie.com/products/robotstack/smart-servo-addon-board/)** is a ready-to-use solution that provides this functionality.

## Structure

```
root directory
     |---python/
          |---src/
               |---dynamixelSDK_websockets/
          |---tests/
               |---protocol1_0/
               |---protocol2_0/
          |---additional-examples/
```

The source code of the library is located in the `python/src/dynamixelSDK_websockets` directory.

The `tests` directory contains examples of using the library with different protocols.

The `additional-examples` directory contains examples demonstrating additional features:

- `send_text.py`: Shows how to send text messages to the server
- `ping_and_poll.py`: Demonstrates how to ping a servo and poll for incoming messages

## Usage

Tested with:

- macOS 24.3.0.
- Python version 3.12.1
- Seeed Xiao ESP32-S3 Microcontroller
- [smart-servo-addon-board](https://github.com/robotstack-dev/smart-servo-addon-board)
- [smart-servo-bridge firmware](https://github.com/robotstack-dev/smart-servo-bridge)
- Dynamixel XL430-W250-T smart servos

### Installation

```bash
$ cd /usr/src/
$ sudo git clone https://github.com/robotstack-dev/dynamixel-python-sdk-websockets
$ sudo chown -R pi dynamixelSDK_websockets
$ cd dynamixelSDK_websockets/python/tests/protocol2_0
$ python3 ping.py
Succeeded to open the port
Succeeded to change the baudrate
[ID:001] ping Succeeded. Dynamixel model number : 1060
```

### Basic Usage

To use WebSocket define your port as:\
&nbsp; &nbsp; &nbsp; &nbsp; `portHandler = PortHandler("ws://yourServerURL:portnum")`\
e.g.:\
&nbsp; &nbsp; &nbsp; &nbsp; `portHandler = PortHandler("ws://192.168.1.22:8080")`

You'll need to find the IP address of the server. If using the smart-servo-bridge firmware, you can print its IP address to the serial monitor when it starts up.

Send binary with:\
&nbsp; &nbsp; &nbsp; &nbsp; `portHandler.writePort([byte1,byte2,...,byteN])`

This feature is used by the Dynamixel SDK with calls such as:\
&nbsp; &nbsp; &nbsp; &nbsp; `packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)`

You can also send text with:\
&nbsp; &nbsp; &nbsp; &nbsp; `portHandler.writePort("my message here")`
