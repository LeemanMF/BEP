\\alleen het gedeelte van python
int incomingData = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

incomingData = Serial.read();
Motor.run(incomingData);

Serial.print("I received: ");
Serial.println(incomingData);
}
