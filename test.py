from servo import Servo, servo2040

import math
import time

FEMUR_LENGTH = 3.0
COXA_LENGTH = 2.272638
TIBIA_LENGTH = 6.0

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar.x, self.y * scalar.y, self.z * scalar.z)  


def getPointOnBezier2D(points, numPoints, t):
    pos = Vector.Vector2D(0, 0)  # Assuming Vector2D class is already defined
# I looked up how to do this on wikipedia as well
    for i in range(numPoints):
        B = Bezier.getBinomialCoefficient(numPoints-1, i) * (1-t)**(numPoints-1-i) * t**i
        pos.x += B * points[i].x
        pos.y += B * points[i].y
    return pos

@staticmethod
def getPointOnBezier3D(points, numPoints, t):
    pos = Vector.Vector3D(0, 0, 0)  # Assuming Vector3D class is already defined
    # I looked up how to do this on wikipedia as well
    for i in range(numPoints):
        B = Bezier.getBinomialCoefficient(numPoints-1, i) * (1-t)**(numPoints-1-i) * t**i
        pos.x += B * points[i].x
        pos.y += B * points[i].y
        pos.z += B * points[i].z
    return pos

def getBinomialCoefficient(n, k):
        # I looked up the formula for this on wikipedia
    result = 1
    for i in range(1, k+1):
        result *= (n-(k-1))
        result //= i
    return result

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
    
        
        