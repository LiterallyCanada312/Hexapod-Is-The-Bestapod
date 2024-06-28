#include <Servo.h>
#include <SPI.h>
#include "init.ino"

#include <Adafruit_PWMServoDriver.h>
#include <Wire.h>

#define Y_OFFSET 7.5
#define Z_OFFSET 5.5
#define FEMUR_LENGTH 3.0
#define COXA_LENGTH 2.272638
#define TIBIA_LENGTH 6.0

#define pi 3.14159

#define SERVOMIN 1000 
#define SERVOMAX 2000

Adafruit_PWMServoDriver pwm0 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x41);

int legs[16] = {};

void setup() {
  // put your setup code here, to run once:

  pwm0.begin();
  pwm0.setOscillatorFrequency(25000000);
  pwm0.setPWMFreq(50);

  pwm1.begin();
  pwm1.setOscillatorFrequency(25000000);
  pwm1.setPWMFreq(50);

  calibStand();

}

void loop() {
  // put your main code here, to run repeatedly:
    
}

void setLegToVector(int leg, Vector3 vec){
    float X = vec.x;
    float Y = vec.y;
    float Z = vec.z;

    Y += Y_OFFSET;
    Z += Z_OFFSET;

    float lL = sqrt(pow(X,2) + pow(Z,2)); // Leg Length
    float hF = sqrt(pow((lL - COXA_LENGTH),2) + pow(y,2)); // length of line that forms triangle with tibia and femur
    float A1 = atan2((lL - COXA_LENGTH)/Y);
    float A2 = acos((pow(TIBIA_LENGTH, 2) - pow(FEMUR_LENGTH, 2) - pow(HF, 2))/(-2*FEMUR_LENGTH*hF));

    float femurAngle = 90 - (A1 + A2);
    float B1 = acos((pow(HF,2)-pow(TIBIA_LENGTH,2)-pow(FEMUR_LENGTH,2))/(-2*FEMUR_LENGTH*TIBIA_LENGTH));

    float tibiaAngle = (90 - B1);
    float coxaAngle = atan2(Z/X);

    float pulseLength1 = map(coxaAngle, 0, 180, SERVOMIN, SERVOMAX);
    float pulseLength2 = map(femurAngle, 0, 180, SERVOMIN, SERVOMAX);
    float pulseLength3 = map(tibiaAngle, 0, 180, SERVOMIN, SERVOMAX);

    if(leg != -1){
      switch(leg){
        
        // TODO: SET UP PROPER LEG GROUPING ON THE PCB

        case 1:

          pwm0.setPwm(0, 0 , pulseLength1);
          pwm0.setPwm(1, 0 , pulseLength2);
          pwm0.setPwm(2, 0, pulseLength3);

          break;

        case 2:

          pwm0.setPwm(3, 0 , pulseLength1);
          pwm0.setPwm(4, 0 , pulseLength2);
          pwm0.setPwm(5, 0, pulseLength3);

          break;

        case 3:

          pwm0.setPwm(6, 0 , pulseLength1);
          pwm0.setPwm(7, 0 , pulseLength2);
          pwm0.setPwm(8, 0, pulseLength3);

          break;

        case 4: 

          pwm1.setPwm(9, 0 , pulseLength1);
          pwm1.setPwm(10, 0 , pulseLength2);
          pwm1.setPwm(11, 0, pulseLength3);

          break;

        case 5:

          pwm1.setPwm(12, 0 , pulseLength1);
          pwm1.setPwm(13, 0 , pulseLength2);
          pwm1.setPwm(14, 0, pulseLength3);

          break;

        case 6:

          pwm1.setPwm(15, 0 , pulseLength1);
          pwm1.setPwm(16, 0 , pulseLength2);
          pwm1.setPwm(17, 0, pulseLength3);

          break;

        default:
          break;

      }
    }
}



