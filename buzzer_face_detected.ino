int greenLed = 13;
int redLed = 12;
char receivedData;

void setup() {
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    receivedData = Serial.read();
    if (receivedData == '1') {
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
    } else if (receivedData == '2') {
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
    }
  }
}