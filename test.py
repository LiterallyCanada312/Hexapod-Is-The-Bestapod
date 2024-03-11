from servo import Servo, servo2040
import Init
import Leg
import Util

import math
import time

FEMUR_LENGTH = 3.0
COXA_LENGTH = 2.272638
TIBIA_LENGTH = 6.0

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

def cartesian_move(X,Y,Z, m1, m2, m3):
    Y+=7.5 #offset Y
    Z-= 5.5 #offset Z
    J1 = math.atan(X/Y) * (180 / math.pi)
    H = math.sqrt((Y * Y) + (X * X))
    L = math.sqrt((H * H) + (Z * Z))
    J3 = 360 - math.acos(constrain((((FEMUR_LENGTH * FEMUR_LENGTH) - (TIBIA_LENGTH * TIBIA_LENGTH) - (L * L))   /   (-2 * FEMUR_LENGTH * TIBIA_LENGTH)   ), -1, 1))*(180 / math.pi)
    B = math.acos(constrain((((L * L) + (FEMUR_LENGTH * FEMUR_LENGTH) - (TIBIA_LENGTH * TIBIA_LENGTH))   /   (2 * L * FEMUR_LENGTH)   ), -1, 1)) * (180 / math.pi)
    A = math.atan(Z / H) * (180 / math.pi) # BECAUSE Z REST IS NEGATIVE, THIS RETURNS A NEGATIVE VALUE
    J2 = (B + A)  # BECAUSE 'A' IS NEGATIVE AT REST WE NEED TO INVERT '-' TO '+'
    m1.value(30- J1)
    m2.value(90-J2)
    print(J3)
    m3.value(J3)

def moveTo(leg, target_vec3):
    curr_leg = legs[leg]

    distance = math.sqrt(math.pow((target_vec3.x),2) + math.pow((target_vec3.y),2) + math.pow((target_vec3.z), 2))
    if distance > FEMUR_LENGTH+COXA_LENGTH+TIBIA_LENGTH:
        return
    
    swtich(leg):
        case 0:
            cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, s1, s2, s3)
            break
        case 1:
            cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, s4, s5, s6)
            break
        case 2: 
            cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, s7, s8, s9)
            break
        case 3:
            cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, s10, s11, s12)
            break
        case 4:
            cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, s13, s14, s15)
            break
        case 5:
            cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, s16, s17, s18)
            break

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

l1 = Leg.Leg(s1, s2, s3, false)
l2 = Leg.Leg(s4, s5, s6, false)
l3 = Leg.Leg(s7, s8, s9, false)
l4 = Leg.Leg(s10, s11, s12, false)
l5 = Leg.Leg(s13, s14, s15, false)
l6 = Leg.Leg(s16, s17, s18, false)

