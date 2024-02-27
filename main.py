from servo import Servo, servo2040
import math
import InverseKinematics


s1 = Servo(servo2040.SERVO_1)
s2 = Servo(servo2040.SERVO_2)
s3 = Servo(servo2040.SERVO_3)

s1.enable()
s2.enable()
s3.enable()

while True:
    x = float(input("X:"))
    y = float(input("Y: "))
    z = float(input("Z: "))

    s1.value(InverseKinematics.getCoxAngle(x,z))
    s2.value(InverseKinematics.getFemurServoAngle(x,y,z))
    s3.value(InverseKinematics.getTibiaServoAngle(x,y,z))

