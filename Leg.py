from servo import Servo, servo2040

import math
import Vector
import Bezier
from Util import constrain

class Leg:

    FEMUR_LENGTH = 3.0
    COXA_LENGTH = 2.272638
    TIBIA_LENGTH = 6.0

    def __init__(self, m1, m2, m3, inverted):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.inverted = inverted
    
    def isInverted():
        return self.inverted

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
        
        if(isInverted):
            self.m1.value(180- J1)
        else:
            self.m1.value(90- J1)
        self.m2.value(90-J2)
        #print(J3)
        self.m3.value(J3)
    
    def moveTo(target_vec3):

        distance = math.sqrt(math.pow((target_vec3.x),2) + math.pow((target_vec3.y),2) + math.pow((target_vec3.z), 2))
        if distance > FEMUR_LENGTH+COXA_LENGTH+TIBIA_LENGTH:
            return
        
        cartesian_move(target_vec3.x, target_vec3.y, target_vec3.z, self.m1, self.m2, self.m3)
