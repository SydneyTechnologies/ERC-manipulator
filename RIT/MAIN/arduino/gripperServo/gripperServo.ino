
#include <Servo.h>
#include <math.h>

// This is the code for controlling the gripper

Servo myservo;
void setup() {
  // put your setup code here, to run once:
   myservo.attach(9);
   Serial.begin(9600);
  //  myservo.write(180);
   Serial.println("Fully closed");
   delay(2000);
  //  myservo.write(90);
   Serial.println("Fully opened");
   Serial.println("Ready, enter angle");
  
}

// float mapRotation(int size, int gripperHeight){
//   float rotationAngle = 180 - (asinf(size / gripperHeight) * 180 / PI);
//   Serial.println(asinf(size / gripperHeight));
//   return rotationAngle;
// }

void loop() {
  // put your main code here, to run repeatedly:
 while (Serial.available()) {
    int gripOpen = Serial.parseInt();
    //  int angle =  map(gripOpen, 0, 17, 30, 180);
     int angle =  map(gripOpen, 14, 0, 0, 50); // This line maps the given width to its corresponsing angle to turn the servo motor
    //  int angle = gripOpen;
    //  int angle = mapRotation(gripOpen, 7.5);
    Serial.println(angle);
     if (angle <= 50 && angle >= 0) {
       if (Serial.read() == '\n') {
         Serial.println(angle);
         myservo.write(angle);
      }
    }
  }
}