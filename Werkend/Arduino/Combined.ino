#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <Arduino.h>
#include <SoftwareSerial.h>

#define ENCA 3 // YELLOW
#define ENCB 2 // WHITE
#define PWM 5
#define IN2 6
#define IN1 7

/* This driver reads raw data from the BNO055

   Connections
   ===========
   Connect SCL to analog 5
   Connect SDA to analog 4
   Connect VDD to 3.3V DC
   Connect GROUND to common ground

   History
   =======
   2015/MAR/03  - First release (KTOWN)
*/
/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (10)

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28, &Wire);

void setup(void)
{
  Serial.begin(230400);
  while (!Serial) delay(10);  // wait for serial port to open!

  // Serial.println("Orientation Sensor Raw Data Test"); Serial.println("");

  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    // Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }


  bno.setExtCrystalUse(true);

  // Serial.println("Calibration status values: 0=uncalibrated, 3=fully calibrated");
  pinMode(ENCA,INPUT);
  pinMode(ENCB,INPUT);
//  attachInterrupt(digitalPinToInterrupt(ENCA),readEncoder,RISING);
  
  pinMode(PWM,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
}
void loop(void)
{
  // Possible vector values can be:
  // - VECTOR_ACCELEROMETER - m/s^2
  // - VECTOR_MAGNETOMETER  - uT
  // - VECTOR_GYROSCOPE     - rad/s
  // - VECTOR_EULER         - degrees
  // - VECTOR_LINEARACCEL   - m/s^2
  // - VECTOR_GRAVITY       - m/s^2
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  imu::Vector<3> gyr = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);

  /* Display the floating point data */
  Serial.print(euler.y());
  Serial.print(",");
  Serial.print(euler.z());
  Serial.print(",");
  Serial.print(gyr.y());
  Serial.print(",");
  Serial.println(gyr.z());
  delay(100);

  // /* Display calibration status for each sensor. */
// if(system < 3);
//   {
//   bno.getCalibration(&system, &gyr);
//   Serial.print("CALIBRATION: Sys=");
//   Serial.print(system, DEC);
//   Serial.print(" Gyro=");
//   Serial.print(gyr, DEC);
////   Serial.print(" Accel=");
////   Serial.print(accel, DEC);
////   Serial.print(" Mag=");
////   Serial.println(mag, DEC);
// }
// 
  // delay(BNO055_SAMPLERATE_DELAY_MS);
  if (Serial.available() > 0) {
  int pps = Serial.readStringUntil(0x0a).toInt();
  // Serial.println(pps, DEC);
  // float pps = 0;
  int dir;
  
  // motor direction
  if(pps<0){
    dir = -1;
    pps = abs(min(pps,0));
    }
  else if(pps>0){
    dir = 1;
    pps = max(0,pps);
    }

  int motor_value = pps;

  // int range = 64000; //max hoeveelheid
  // int motor_value = pps*255/range;

// signal the motor
  setMotor(dir,motor_value,PWM,IN1,IN2);

  }
  
}


void setMotor(int dir, int motor_value, int pwm, int in1, int in2){
  analogWrite(pwm,motor_value);
  if(dir == 1){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
  }
  else if(dir == -1){
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
  }
  else{
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
  }  
}
  
