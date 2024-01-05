import serial
import time
SERVO_PORT = "/dev/cu.usbmodem140"

arduino = serial.Serial(port=SERVO_PORT, timeout=0, baudrate=9600)
# arduino2 = serial.Serial(port=SERVO_PORT, timeout=0, baudrate=9600)


def checkDistance():
    arduino.write(str.encode("s"))
    time.sleep(2)
    print("buffering")
    while True: 
        # if arduino.in_waiting > 0:  # check if there's data in the serial buffer
            arduino.write(str.encode("s\n"))
            time.sleep(1) 
            if arduino.in_waiting > 0:
                data = arduino.readline().strip() 
                print("DISTANCE gotten:", arduino.readline())
                print("DISTANCE IS:", data) 
                distance = int(data)
                return distance
        

checkDistance()