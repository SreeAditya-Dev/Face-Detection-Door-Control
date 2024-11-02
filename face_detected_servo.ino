#include <Servo.h>

Servo myServo; // Create a Servo object
int ledPin = 13; // Pin number for the LED
char receivedData;

void setup() {
  pinMode(ledPin, OUTPUT);
  myServo.attach(9); // Attach the servo motor to pin 9
  myServo.write(0);  // Start with the door closed (0 degrees)
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    receivedData = Serial.read();
    if (receivedData == '1') {
      myServo.write(90); // Open the door (90 degrees)
      digitalWrite(ledPin, LOW); // Turn off the LED
    } else if (receivedData == '2') {
      myServo.write(0); // Close the door (0 degrees)
      digitalWrite(ledPin, HIGH); // Turn on the LED
    }
  }
}
