from servo import Servo, servo2040
from Init import init
import Leg
import Util

import math
import time


walkCoords = [
            [-2, 8, 00.0],
            [-5, 5, 00.0],
            [-10, 10, 00.0],
            [-8, 2, 15.0],
            [-5, 5, 25.0],
            [0.0, 10, 30.0],
            [5, 15, 25.0],
            [8, 18, 15.0],
            [10, 20, 00.0],
            [5, 15, 00.0],
            [2, 12, 00.0],
            [0.0, 10, 00.0],
        ]

s1 = Servo(servo2040.SERVO_1)
s2 = Servo(servo2040.SERVO_2)
s3 = Servo(servo2040.SERVO_3)
s4 = Servo(servo2040.SERVO_1)
s5 = Servo(servo2040.SERVO_2)
s6 = Servo(servo2040.SERVO_3)
s7 = Servo(servo2040.SERVO_1)
s8 = Servo(servo2040.SERVO_2)
s9 = Servo(servo2040.SERVO_3)
s10 = Servo(servo2040.SERVO_1)
s11 = Servo(servo2040.SERVO_2)
s12 = Servo(servo2040.SERVO_3)
s13 = Servo(servo2040.SERVO_1)
s14 = Servo(servo2040.SERVO_2)
s15 = Servo(servo2040.SERVO_3)
s16 = Servo(servo2040.SERVO_1)
s17 = Servo(servo2040.SERVO_2)
s18 = Servo(servo2040.SERVO_3)

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

