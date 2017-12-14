import Server.RaspberryPiControl.RPi.GPIO as GPIO


class PiControl:
    def __init__(self):
        pass

    R1 = None
    R2 = None

    L2 = None
    L1 = None

    PIN_STATE_MAP = {}
    GPIOLOW = 0
    GPIOHIGH = 1

    def setup_pi_for_movement(self):
        self.R1 = 26
        self.R2 = 20

        self.L2 = 19
        self.L1 = 16

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.R1, GPIO.OUT)
        GPIO.setup(self.R2, GPIO.OUT)

        GPIO.setup(self.L2, GPIO.OUT)
        GPIO.setup(self.L1, GPIO.OUT)

        self.PIN_STATE_MAP = {self.R1: 0, self.R2: 0,
                         self.L2: 0, self.L1: 0}

    def move_forward(self, x):
        GPIO.output(self.R1, GPIO.HIGH)
        GPIO.output(self.L1, GPIO.HIGH)

    def move_backward(self, x):
        GPIO.output(self.R2, GPIO.HIGH)
        GPIO.output(self.L2, GPIO.HIGH)

    def move_stop(self):
        GPIO.output(self.R1, GPIO.LOW)
        GPIO.output(self.R2, GPIO.LOW)
        GPIO.output(self.L1, GPIO.LOW)
        GPIO.output(self.L2, GPIO.LOW)

    def rotate_right(self, x):
        GPIO.output(self.R1, GPIO.HIGH)

    def rotate_left(self, x):
        GPIO.output(self.L1, GPIO.HIGH)

    def rotate_stop(self):
        GPIO.output(self.R1, GPIO.LOW)
        GPIO.output(self.L1, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

class PinState:
    number = None
    state = 0

    def __init__(self, number_param):
        global number
        number = number_param
