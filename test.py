from servo import Servo, servo2040
import Leg
import Util 
import Vector

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


l1 = Leg.leg(s1, s2, s3)
l2 = Leg.leg(s4, s5, s6)
l3 = Leg.leg(s7, s8, s9)
l4 = Leg.leg(s10, s11, s12)
l5 = Leg.leg(s13, s14, s15)
l6 = Leg.leg(s16, s17, s18)

Legs = []
Legs.append(l1)
Legs.append(l2)
Legs.append(l3)
Legs.append(l4)
Legs.append(l5)
Legs.append(l6)

legsInitialized = 0
for leg in Legs:
    leg.standFromRest()
    print(legsInitialized + " stood")
    legsInitialized += 1

time.sleep(5)

        
