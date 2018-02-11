import struct
import serial

class ArdiunoControl:

    def __init__(self):
        self.serialConnection = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)

    def move(self, rotate, move):
        self.serialConnection.write(struct.pack('>BBB',
                                                self.cast_controls_speed_to_int(rotate),
                                                self.cast_controls_speed_to_int(move)))

    def cast_controls_speed_to_int(self, speed_string):
        try:
            speed = int(speed_string)
        except Exception as e:
            return None
        return speed
