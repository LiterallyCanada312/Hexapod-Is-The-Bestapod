from servo import Servo, servo2040
import Init
import Leg
import Util 
import Vector

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

l1 = Leg.Leg(s1, s2, s3, False)
l2 = Leg.Leg(s4, s5, s6, True)
l3 = Leg.Leg(s7, s8, s9, False)
l4 = Leg.Leg(s10, s11, s12, False)
l5 = Leg.Leg(s13, s14, s15, True)
l6 = Leg.Leg(s16, s17, s18, False)


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

def init():
    l1.moveTo(Vector.Vector3D(-2, 8, 00.0))
    l2.moveTo(Vector.Vector3D(-2, 8, 00.0))
    l3.moveTo(Vector.Vector3D(-2, 8, 00.0))
    l4.moveTo(Vector.Vector3D(-2, 8, 00.0))
    l5.moveTo(Vector.Vector3D(-2, 8, 00.0))
    l6.moveTo(Vector.Vector3D(-2, 8, 00.0))

init()

isFinished = False
stepsA = 0
stepsB = 6

while True:

    if(stepsA > 11):
        stepsA = 0
    if(stepsB > 11):
        stepsB = 0 

    if(isFinished is False):
        l1.moveTo(Util.vectorize(walkCoords[stepsA]))
        l2.moveTo(Util.vectorize(walkCoords[stepsB]))
        l3.moveTo(Util.vectorize(walkCoords[stepsA]))
        l4.moveTo(Util.vectorize(walkCoords[stepsB]))
        l5.moveTo(Util.vectorize(walkCoords[stepsA]))
        l6.moveTo(Util.vectorize(walkCoords[stepsB]))

    stepsA += 1
    stepsB += 1