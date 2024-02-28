from servo import Servo, servo2040

import math
import time

FEMUR_LENGTH = 3.0
COXA_LENGTH = 2.272638
TIBIA_LENGTH = 6.0

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

def cartesian_move(X,Y,Z):
    Y+=7.5 #offset Y
    Z-= 5.5 #offset Z
    J1 = math.atan(X/Y) * (180 / math.pi)
    H = math.sqrt((Y * Y) + (X * X));
    L = math.sqrt((H * H) + (Z * Z));
    J3 = 360 - math.acos(constrain((((FEMUR_LENGTH * FEMUR_LENGTH) - (TIBIA_LENGTH * TIBIA_LENGTH) - (L * L))   /   (-2 * FEMUR_LENGTH * TIBIA_LENGTH)   ), -1, 1))*(180 / math.pi)
    B = math.acos(constrain((((L * L) + (FEMUR_LENGTH * FEMUR_LENGTH) - (TIBIA_LENGTH * TIBIA_LENGTH))   /   (2 * L * FEMUR_LENGTH)   ), -1, 1)) * (180 / math.pi)
    A = math.atan(Z / H) * (180 / math.pi) # BECAUSE Z REST IS NEGATIVE, THIS RETURNS A NEGATIVE VALUE
    J2 = (B + A)  # BECAUSE 'A' IS NEGATIVE AT REST WE NEED TO INVERT '-' TO '+'
    s1.value(30- J1)
    s2.value(90-J2)
    print(J3)
    s3.value(J3)


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

s1.enable()
s2.enable()
s3.enable()

s1.value(0)
s2.value(0)
s3.value(0)

while True:
    for coords in walkCoords:
        cartesian_move(coords[0], coords[1], coords[2])
        time.sleep(0.05)
    
        
        