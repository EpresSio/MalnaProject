import sys
import socket
import threading
import re
from Libs import Camera, Control

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", 5005))
server_socket.listen(1)

username = "Ricsi"
password = "3.14"

access = False;

control = Control.Control()

print "Program start"


def camera_capture(camera_socket):
    camera = Camera.Camera(camera_socket)
    camera.capture()


def recv(client_socket):
    while 1:
        try:
            message = client_socket.recv(1024)
            searchResult = re.search("CONTROL_(.+)::(.+)", message)
            if searchResult != None:
                global control
                controlString = searchResult.groups()
                if len(controlString) == 2:
                    if controlString[0] == "M":
                        speed = control.castControsSpeedToInt(controlString[1])
                        if speed == None:
                            client_socket.send(">" + controlString[0] + "_Speed: "
                                               + controlString[1] + " is not a valid integer" + "\n")
                            continue
                        control.modifieMoveSpeed(speed)
                        client_socket.send(">Current " + controlString[0]
                                           + "speed:" + controlString[1] + "\n")
                    elif controlString[0] == "R":
                        speed = control.castControsSpeedToInt(controlString[1])
                        if speed == None:
                            client_socket.send(">" +controlString[0] + "_Speed: "
                                               + controlString[1] + " is not a valid integer" + "\n")
                            continue
                        control.modifieRotateSpeed(controlString[1])
                        client_socket.send(">Current " + controlString[0]
                                           + "speed:" + controlString[1] + "\n")
        except Exception as e:
            sys.exit(0)


def checkAccess(client_socket):
    message = client_socket.recv(1024)
    global access
    searchResult = re.search("LOGIN_(.+)::(.+)", message)
    if searchResult != None:
        accessStrings = searchResult.groups()
        if len(accessStrings) == 2 \
                and accessStrings[0] == username and accessStrings[1] == password:
                access = True
    if not access:
        client_socket.send("ACCESS_DENIED\n")

while 1:
    try:
        print "Waiting for client"
        client_socket, address = server_socket.accept()
        print "Conencted to - ", address, "\n"
        client_socket.send("CONNECTED\n")
        while not access:
            checkAccess(client_socket)
        client_socket.send("ACCESS_GRANTED\n")
        camera_socket, address = server_socket.accept()
        print "Camera port opened\n"
        thread2 = threading.Thread(target=camera_capture, args=[camera_socket])
        thread2.start()
        thread1 = threading.Thread(target=recv, args=[client_socket])
        thread1.start()
        sys.exit(0)
    except socket.timeout:
        continue
