// This is the code for controlling the gripper and getting distance from LIDAR
// expecting command from Python: G0/G10/G20/G30/G50 for gripper opening angle, or L to get LIDAR distance
// Serial speed to PC is 9600, CR/LF does not matter

#include <Servo.h>
#include <math.h>
#include <SoftwareSerial.h>
#include <TFMini.h>


String msg;
uint16_t dist;

int minAngle = 7;   // gripper fully open
int maxAngle = 45;  // gripper fully closed

//SoftwareSerial mySerial(10, 11);
//TFMini tfmini;
Servo myservo;
int trig = 10;
int echo = 11;
long duration;
int distance;

void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  // mySerial.begin(115200);
  // tfmini.begin(&mySerial);
  // put your setup code here, to run once:
  myservo.attach(9);
  Serial.begin(9600);
  // check the servo opening & closing

  myservo.write(maxAngle);
  Serial.println("Gripper fully closed");
  delay(1000);
  myservo.write(minAngle);
  Serial.println("Gripper fully opened");

  // check the LIDAR function
  // dist = tfmini.getDistance();
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance = duration * 0.34 / 2;
  // Serial.print("Sonar distance (cm) = ");
  Serial.println(distance);
  Serial.println("Ready, enter command (eg: 'G10/G20/G30/G40/G50' or 'L')");  // case insensitive
}

void loop() {
  // put your main code here, to run repeatedly:

  while (Serial.available()) {
    msg = "Invalid command";
    String command = Serial.readString();
    command.trim();         // get rid of extra spaces or CR/LF if there's any
    command.toLowerCase();  // always convert to lowercase (case insensitive)

    if (command == "sonar" || command == "s") {
      digitalWrite(trig, LOW);
      delayMicroseconds(2);
      digitalWrite(trig, HIGH);
      delayMicroseconds(10);
      digitalWrite(trig, LOW);
      duration = pulseIn(echo, HIGH);
      distance = duration * 0.34 / 2;
      msg = String(distance);
    }
    if (command == "gripper 0" || command == "g0") {  // fully open
      myservo.write(7);
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
      myservo.write(45);
      msg = "Gripper 50 fully closed";
    }
    Serial.println(msg);
  }
  delay(10);
}
