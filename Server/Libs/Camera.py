import cv2
import socket
import base64


class Camera(object):
    def __init__(self, client_socket):
        print(client_socket)
        self.socket = client_socket
        self.camera = cv2.VideoCapture(0)
        self.camera.set(3, 1920)
        self.camera.set(4, 1080)

    def capture(self):
        while 1:
            try:
                ret, frame = self.camera.read()
                data = cv2.imencode('.jpg', frame)[1].tostring()
                data = base64.encodestring(data)
                data = data.replace("\n", "")
                data = "%s%s%s" % (">", data, "\n")
                success = self.send(self.socket, data)
                if success == 0:
                    break

            except KeyboardInterrupt:
                self.camera.release()

    def send(self, c, data):
        try:
            c.send(data)
            return 1

        except socket.error:
            self.camera.release()
            try:
                self.socket.remove(c)
            except Exception as e:
                print "Client leave without say good-bye :("
            return 0
