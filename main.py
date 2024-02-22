from servo import Servo, servo2040
import math

FEMUR_LENGTH = 3.0
COXA_LENGTH = 2.272638
TIBIA_LENGTH = 6.0

def getFemurServoAngle(x, y, z):
        L = math.sqrt(y*y + z*z)
        A = math.atan(z / y)
        B = math.acos((L*L + FEMUR_LENGTH*FEMUR_LENGTH - TIBIA_LENGTH*TIBIA_LENGTH) / (2*L*FEMUR_LENGTH))
        return B + (-A)

def getTibiaServoAngle(x, y, z):
    L = math.sqrt(y*y + z*z)
    return math.acos((TIBIA_LENGTH*TIBIA_LENGTH + FEMUR_LENGTH*FEMUR_LENGTH - L*L) / (2*FEMUR_LENGTH*TIBIA_LENGTH))
    
def getCoxAngle(x,z):
    return math.atan(z/x)

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

    s1.value(getCoxAngle(x,z))
    s2.value(getFemurServoAngle(x,y,z))
    s3.value(getTibiaServoAngle(x,y,z))

