
class Control(object):

    def modifieMoveSpeed(self, speed):
        print speed

    def modifieRotateSpeed(self, speed):
        print speed


    def castControsSpeedToInt(self, speedString):
        try:
            speed = int(speedString)
        except Exception as e:
            return None
        return speed