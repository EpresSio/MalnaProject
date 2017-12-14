import PiControl


class Control(object):
    PiControl = None

    def __init__(self):
        self.PiControl = PiControl.PiControl()

    def modify_move_speed(self, speed):
        if speed > 0:
            self.PiControl.move_forward(100)
        elif speed < 0:
            self.PiControl.move_backward(100)
        else:
            self.PiControl.move_stop()

    def modify_rotate_speed(self, speed):
        if speed > 0:
            self.PiControl.rotate_right(100)
        elif speed < 0:
            self.PiControl.rotate_left(100)
        else:
            self.PiControl.rotate_stop()

    @staticmethod
    def cast_controls_speed_to_int(speed_string):
        try:
            speed = int(speed_string)
        except Exception as e:
            return None
        return speed
