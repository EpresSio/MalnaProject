import RPi.GPIO as GPIO


class PiControl:
    def __init__(self):
        pass

    Forward = None
    Backward = None

    Right = None
    Left = None

    PIN_STATE_MAP = {}
    GPIOLOW = 0
    GPIOHIGH = 1

    def setup_pi_for_movement(self):
        self.Forward = 26
        self.Backward = 20

        self.Right = 19
        self.Left = 16

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Forward, GPIO.OUT)
        GPIO.setup(self.Backward, GPIO.OUT)

        GPIO.setup(self.Right, GPIO.OUT)
        GPIO.setup(self.Left, GPIO.OUT)

        PIN_STATE_MAP = {self.Forward: 0, self.Backward: 0,
                         self.Right: 0, self.Left: 0}

    def move_forward(self, x):
        if self.PIN_STATE_MAP[self.Backward] != 0:
            GPIO.output(self.Backward, GPIO.LOW)
        if self.PIN_STATE_MAP[self.Forward] != 1:
            GPIO.output(self.Forward, GPIO.HIGH)

    def move_backward(self, x):
        if self.PIN_STATE_MAP[self.Forward] != 0:
            GPIO.output(self.Forward, GPIO.LOW)
        if self.PIN_STATE_MAP[self.Backward] != 1:
            GPIO.output(self.Backward, GPIO.HIGH)

    def move_stop(self):
        if self.PIN_STATE_MAP[self.Forward] != 0:
            GPIO.output(self.Forward, GPIO.LOW)
        if self.PIN_STATE_MAP[self.Backward] != 0:
            GPIO.output(self.Backward, GPIO.LOW)

    def rotate_right(self, x):
        if self.PIN_STATE_MAP[self.Left] != 0:
            GPIO.output(self.Left, GPIO.LOW)
        if self.PIN_STATE_MAP[self.Right] != 1:
            GPIO.output(self.Right, GPIO.HIGH)

    def rotate_left(self, x):
        if self.PIN_STATE_MAP[self.Right] != 0:
            GPIO.output(self.Right, GPIO.LOW)
        if self.PIN_STATE_MAP[self.Left] != 1:
            GPIO.output(self.Left, GPIO.HIGH)

    def rotate_stop(self):
        if self.PIN_STATE_MAP[self.Right] != 0:
            GPIO.output(self.Right, GPIO.LOW)
        if self.PIN_STATE_MAP[self.Left] != 0:
            GPIO.output(self.Left, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

class PinState:
    number = None
    state = 0

    def __init__(self, number_param):
        global number
        number = number_param
