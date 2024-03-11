from servo import Servo, servo2040
import Init
import Leg
import Util

import math
import time


s1 = Servo(servo2040.SERVO_1)
s2 = Servo(servo2040.SERVO_2)
s3 = Servo(servo2040.SERVO_3)
s4 = Servo(servo2040.SERVO_4)
s5 = Servo(servo2040.SERVO_5)
s6 = Servo(servo2040.SERVO_6)
s7 = Servo(servo2040.SERVO_7)
s8 = Servo(servo2040.SERVO_8)
s9 = Servo(servo2040.SERVO_9)
s10 = Servo(servo2040.SERVO_10)
s11 = Servo(servo2040.SERVO_11)
s12 = Servo(servo2040.SERVO_12)
s13 = Servo(servo2040.SERVO_13)
s14 = Servo(servo2040.SERVO_14)
s15 = Servo(servo2040.SERVO_15)
s16 = Servo(servo2040.SERVO_16)
s17 = Servo(servo2040.SERVO_17)
s18 = Servo(servo2040.SERVO_18)

s1.enable()
s2.enable()
s3.enable()
s4.enable()
s5.enable()
s6.enable()
s7.enable()
s8.enable()
s9.enable()
s10.enable()
s11.enable()
s12.enable()
s13.enable()
s14.enable()
s15.enable()
s16.enable()
s17.enable()
s18.enable()

l1 = Leg.Leg(s1, s2, s3, false)
l2 = Leg.Leg(s4, s5, s6, false)
l3 = Leg.Leg(s7, s8, s9, false)
l4 = Leg.Leg(s10, s11, s12, false)
l5 = Leg.Leg(s13, s14, s15, false)
l6 = Leg.Leg(s16, s17, s18, false)

