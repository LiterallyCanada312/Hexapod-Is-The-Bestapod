#include <Servo.h>
#include <nRF24L01>
#include <SPI.h>

#include <Adafruit_PWMServoDriver.h>
#include <Wire.h>

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
