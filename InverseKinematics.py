import math

FEMUR_LENGTH = 3.0
COXA_LENGTH = 2.272638
TIBIA_LENGTH = 6.0

class InverseKinematics:

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
    