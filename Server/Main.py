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

pre_string = ">>MalnaProject ::"

access = False

control = Control.Control()

print pre_string, "Start"


def camera_capture(camera_socket_param):
    camera = Camera.Camera(camera_socket_param)
    camera.capture()


def recv(client_socket_param, address):
    while 1:
        try:
            message = client_socket_param.recv(1024)
            print message
            search_result = re.search("CONTROL_(.+)::(.+)", message)
            if search_result is not None:
                global control
                control_string = search_result.groups()
                if len(control_string) == 2:
                    if control_string[0] == "M":
                        speed = control.cast_controls_speed_to_int(control_string[1])
                        if speed is None:
                            client_socket_param.send(">" + control_string[0] + "_Speed: "
                                                     + control_string[1] + " is not a valid integer" + "\n")
                            continue
                        control.modify_move_speed(speed)
                        client_socket_param.send(">Current " + control_string[0]
                                                 + "speed:" + control_string[1] + "\n")
                    elif control_string[0] == "R":
                        speed = control.cast_controls_speed_to_int(control_string[1])
                        if speed is None:
                            client_socket_param.send(">" + control_string[0] + "_Speed: "
                                                     + control_string[1] + " is not a valid integer" + "\n")
                            continue
                        control.modify_rotate_speed(speed)
                        client_socket_param.send(">Current " + control_string[0]
                                                 + "speed:" + control_string[1] + "\n")
        except Exception as e:
            print "Something wrong"
        # control.PiControl.cleanup()
        # client_socket_param.shutdown(0)
        # client_socket_param.close()
        # print pre_string, "Disconnected from - ", address
        # return


def check_access(client_socket_param):
    message = client_socket_param.recv(1024)
    global access
    search_result = re.search("LOGIN_(.+)::(.+)", message)
    if search_result is not None:
        access_strings = search_result.groups()
        if len(access_strings) == 2 \
                and access_strings[0] == username and access_strings[1] == password:
            access = True
    if not access:
        client_socket_param.send("ACCESS_DENIED\n")


while 1:
    try:
        print pre_string, "Waiting for client"
        client_socket, address = server_socket.accept()
        print pre_string, "Connected to - ", address
        client_socket.send("CONNECTED\n")
        while not access:
            check_access(client_socket)
        client_socket.send("ACCESS_GRANTED\n")
        camera_socket, address = server_socket.accept()
        print pre_string, "Camera port opened\n"
        thread2 = threading.Thread(target=camera_capture, args=[camera_socket])
        thread2.start()
        thread1 = threading.Thread(target=recv, args=[client_socket, address])
        thread1.start()
    except socket.timeout:
        continue
