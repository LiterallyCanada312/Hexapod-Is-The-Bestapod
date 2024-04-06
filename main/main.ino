#include <Servo.h>
#include <nRF24L01>
#include <SPI.h>

#include <Adafruit_PWMServoDriver.h>
#include <Wire.h>

#define Y_OFFSET 7.5
#define Z_OFFSET 5.5
#define FEMUR_LENGTH 3.0
#define COXA_LENGTH 2.272638
#define TIBIA_LENGTH 6.0

#define pi 3.14159

Adafruit_PWMServoDriver pwm0 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x41);

void setup() {
  // put your setup code here, to run once:

  pwm0.begin();
  pwm0.setOscillatorFrequency(25000000);
  pwm0.setPWMFreq(50);

  pwm1.begin();
  pwm1.setOscillatorFrequency(25000000);
  pwm1.setPWMFreq(50);

}

void loop() {
  // put your main code here, to run repeatedly:

}

void setAngle(int leg, Vector3 vec){
    float X = vec.x;
    float Y = vec.y;
    float Z = vec.z;

    Y += Y_OFFSET;
    Z += Z_OFFSET;

     J1 = math.atan(X/Y) * (180 / pi);
     H = math.sqrt((Y * Y) + (X * X));
     L = math.sqrt((H * H) + (Z * Z));
     J3 = 360 - math.acos(constrain((((FEMUR_LENGTH * FEMUR_LENGTH) - (TIBIA_LENGTH * TIBIA_LENGTH) - (L * L))   /   (-2 * FEMUR_LENGTH * TIBIA_LENGTH)   ), -1, 1))*(180 / pi);
     B = math.acos(constrain((((L * L) + (FEMUR_LENGTH * FEMUR_LENGTH) - (TIBIA_LENGTH * TIBIA_LENGTH))   /   (2 * L * FEMUR_LENGTH)   ), -1, 1)) * (180 / math.pi);
     A = math.atan(Z / H) * (180 / pi);
     J2 = (B + A);


}

