import struct
import serial
import threading
import serial.tools.list_ports


class ArdiunoControl:
    def __init__(self):
        list = serial.tools.list_ports.comports()
        connected = []
        for element in list:
            connected.append(element[0])
        if len(connected) == 0:
            return
        self.serialConnection = serial.Serial(connected[0], 115200, timeout=.5)
        recv = threading.Thread(target=self.recvt, args=[self.serialConnection])
        recv.start()

    def move(self, rotate, move):
        try:
            rotate = self.cast_controls_speed_to_int(rotate)
            rotate = (rotate + 1) / 2 * 125 + 25  # [-1-1] -> [25-155]
            move = self.cast_controls_speed_to_int(move)
            direction = move
            if direction != 0:
                direction = direction / abs(move)
            speed = abs(move) * 250  # [0-1] -> [0-250]
            if direction == -1:
                direction = 2
        except ValueError:
            return
        self.serialConnection.write(struct.pack('>BBBB',
                                                255, int(rotate), int(direction), int(speed)))
        self.serialConnection.flushOutput()

    def cast_controls_speed_to_int(self, speed_string):
        try:
            speed = float(speed_string)
        except ValueError as e:
            return None
        return speed

        # serialConnection = serial.Serial('/dev/ttyACM1', 115200, timeout=.1)
        # while(True) :
        #     serialConnection.write(struct.pack('>BBB',
        #                                         int(raw_input("r")), int(raw_input("d")), int(raw_input("s"))))

    def recvt(self, connect):
        while 1:
            data = connect.readline()
            if data:
                print data
