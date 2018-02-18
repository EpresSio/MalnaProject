import struct
import serial


class ArdiunoControl:
    def __init__(self):
        self.serialConnection = serial.Serial('/dev/ttyACM2', 115200, timeout=.1)

    def move(self, rotate, move):
        rotate = self.cast_controls_speed_to_int(rotate)
        rotate = (rotate + 1) / 2 * 125 + 25  # [-1-1] -> [25-155]
        move = self.cast_controls_speed_to_int(move)
        direction = move
        if direction != 0:
            direction = direction / abs(move)
        speed = abs(move) * 250  # [0-1] -> [0-250]
        print rotate, direction, speed
        self.serialConnection.write(struct.pack('>BBB',
                                                int(rotate), int(direction), int(speed)))

    def cast_controls_speed_to_int(self, speed_string):
        try:
            speed = float(speed_string)
        except Exception as e:
            return None
        return speed
