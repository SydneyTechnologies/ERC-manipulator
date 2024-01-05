import socket
from time import sleep

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("192.168.150.2",2001))


def sendToEpson(x = 0, y = 450, robot_z = 750, robot_u = 0):
    coordinates = "GO " + f"{x} {y} {robot_z} {robot_u}" + "\r\n"
    print (f"Sending to position {x}, {y}")
    clientSocket.send(coordinates.encode())
    confirmation = clientSocket.recv(1023) # waiting for confirmation from robot
    print("result:", confirmation)
    sleep(1)

def Home():
    sendToEpson(0, 450, 850, 90)


clientSocket.close 