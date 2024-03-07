from servo import Servo, servo2040
from test import legs, moveTo
from Vector import Vector3D
import Bezier

# Tripod Control Point Array

TCPA = [
    Vector3D(),
    Vector3D(), 
    Vector3D(),
    Vector3D(),
    Vector3D(),
    Vector3D()
]

TIBCPA = [] # Tripod In Between Control Point Array 

