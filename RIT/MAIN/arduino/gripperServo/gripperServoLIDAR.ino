// This is the code for controlling the gripper and getting distance from LIDAR
// expecting command from Python: G0/G10/G20/G30/G50 for gripper opening angle, or L to get LIDAR distance
// Serial speed to PC is 9600, CR/LF does not matter

#include <Servo.h>
#include <math.h>
#include <SoftwareSerial.h>
#include <TFMini.h>


String msg;
uint16_t dist;

int minAngle = 0;   // gripper fully open
int maxAngle = 50;  // gripper fully closed

SoftwareSerial mySerial(10, 11);
TFMini tfmini;
Servo myservo;

void setup() {
  mySerial.begin(115200);
  tfmini.begin(&mySerial);
  // put your setup code here, to run once:
  myservo.attach(9);
  Serial.begin(9600);
  // check the servo opening & closing
  myservo.write(minAngle);
  Serial.println("Gripper fully opened");
  delay(2000);
  myservo.write(maxAngle);
  Serial.println("Gripper fully closed");
  // check the LIDAR function
  dist = tfmini.getDistance();
  Serial.print("LIDAR distance (cm) = ");
  Serial.println(dist);
  Serial.println("Ready, enter command (eg: 'G10/G20/G30/G40/G50' or 'L')"); // case insensitive
}

void loop() {
  // put your main code here, to run repeatedly:

  while (Serial.available()) {
    msg = "Invalid command";
    String command = Serial.readString();
    command.trim();         // get rid of extra spaces or CR/LF if there's any
    command.toLowerCase();  // always convert to lowercase (case insensitive)

    if (command == "lidar" || command == "l") {
      for (int x=0; x<5; x++) { // make 5x reading for reliability
        dist = tfmini.getDistance();
        delay(50);
      }
      msg = "LIDAR distance in cm = " + String(dist);
    }
    if (command == "gripper 0" || command == "g0") {  // fully open
      myservo.write(0);
      msg = "Gripper 0 fully opened";
    }
    if (command == "gripper 10" || command == "g10") {  
      myservo.write(10);
      msg = "Gripper 10";
    }
    if (command == "gripper 20" || command == "g20") {
      myservo.write(20);
      msg = "Gripper 20";
    }
    if (command == "gripper 30" || command == "g30") {
      myservo.write(30);
      msg = "Gripper 30";
    }
    if (command == "gripper 40" || command == "g40") {
      myservo.write(40);
      msg = "Gripper 40";
    }
    if (command == "gripper 50" || command == "g50") {  // fully closed
      myservo.write(50);
      msg = "Gripper 50 fully closed";
    }
    Serial.println(msg);
    Serial.println("OK");
  }
  delay(10);
}

