import RPi.GPIO as GPIO


class PiControl:
    def __init__(self):
        pass

    R1 = 26
    R2 = 20

    L2 = 21
    L1 = 16

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)

    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L1, GPIO.OUT)

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
