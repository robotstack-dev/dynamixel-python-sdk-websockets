import time
import sys
import websocket

LATENCY_TIMER = 16
DEFAULT_BAUDRATE = 115200

class PortHandler:
    def __init__(self, websocket_url):
        self.is_open = False
        self.baudrate = DEFAULT_BAUDRATE
        self.packet_start_time = 0.0
        self.packet_timeout = 0.0
        self.tx_time_per_byte = 0.0

        self.is_using = False
        self.websocket_url = websocket_url
        self.websocket = None
        self.buffer = b""  # Buffer to store excess data from previous reads

    def openPort(self):
        # Opens a connection to the WebSocket server
        return self.setBaudRate(self.baudrate)

    def closePort(self):
        # Closes the WebSocket connection
        if self.websocket:
            self.websocket.close()
            self.is_open = False

    def clearPort(self):
        # Clear any buffer or state, WebSockets don't use buffers in the same way as serial
        pass

    def setPortName(self, websocket_url):
        # If URL changes and port is open, reconnect
        if self.websocket_url != websocket_url and self.is_open:
            self.closePort()
        
        self.websocket_url = websocket_url
        if self.is_open:
            self.openPort()

    def getPortName(self):
        return self.websocket_url

    def setBaudRate(self, baudrate):
        baud = self.getCFlagBaud(baudrate)
        if baud <= 0:
            return False
        else:
            self.baudrate = baudrate
            return self.setupPort()

    def getBaudRate(self):
        return self.baudrate

    def getBytesAvailable(self):
        # WebSocket doesn't have a direct equivalent to check available bytes
        return 0

    def readPort(self, length):
        try:
            # Check if buffer has enough data to fulfill the request
            if len(self.buffer) >= length:
                # If yes, slice the buffer and update it with remaining data
                data, self.buffer = self.buffer[:length], self.buffer[length:]
                return data

            # If buffer doesn't have enough data, attempt to receive more from WebSocket
            if self.websocket:
                received_data = self.websocket.recv()
                
                # Add new data to buffer
                self.buffer += received_data

                # If buffer now has enough data, slice and update it
                if len(self.buffer) >= length:
                    data, self.buffer = self.buffer[:length], self.buffer[length:]
                    return data

                # If not enough data even after recv, return whatever is in the buffer and clear it
                data, self.buffer = self.buffer, b""
                return data

        except Exception as e:
            print(f"Read error: {e}")
        
        return None

    def writePort(self, packet):
        try:
            if self.websocket:
                self.websocket.send_binary(packet)
                return len(packet)
        except Exception as e:
            print(f"Write error: {e}")
        return 0

    def setPacketTimeout(self, packet_length):
        self.packet_start_time = self.getCurrentTime()
        self.packet_timeout = (self.tx_time_per_byte * packet_length) + (LATENCY_TIMER * 2.0) + 2.0

    def setPacketTimeoutMillis(self, msec):
        self.packet_start_time = self.getCurrentTime()
        self.packet_timeout = msec

    def isPacketTimeout(self):
        if self.getTimeSinceStart() > self.packet_timeout:
            self.packet_timeout = 0
            return True
        return False

    def getCurrentTime(self):
        return round(time.time() * 1000000000) / 1000000.0

    def getTimeSinceStart(self):
        time_since = self.getCurrentTime() - self.packet_start_time
        if time_since < 0.0:
            self.packet_start_time = self.getCurrentTime()
        return time_since

    def setupPort(self):
        if self.is_open:
            self.closePort()

        try:
            self.websocket = websocket.create_connection(self.websocket_url)
            self.is_open = True
            self.tx_time_per_byte = (1000.0 / self.baudrate) * 10.0
            return True
        except Exception as e:
            print(f"Failed to connect to WebSocket: {e}")
            self.is_open = False
            return False

    def getCFlagBaud(self, baudrate):
        # Keep baudrate method for compatibility, though not needed in WebSockets
        if baudrate in [
            9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000, 
            576000, 921600, 1000000, 1152000, 2000000, 2500000, 3000000, 
            3500000, 4000000
        ]:
            return baudrate
        else:
            return -1
        
    # use for debugging packets...don't use by default
    def hexdump(self, src, length):
        print("[HEXDUMP] ", len(src), " bytes:")
        print("bytes expected: ", length, ", received: ", len(src))
        for i in range(len(src)):
            print(hex(src[i]), end=" ")
        print("\n")
    
