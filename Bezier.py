import Vector

class Bezier:

    def getPointOnBezier2D(points, numPoints, t):
        pos = Vector.Vector2D(0, 0)  # Assuming Vector2D class is already defined
        # I looked up how to do this on wikipedia as well
        for i in range(numPoints):
            B = Bezier.getBinomialCoefficient(numPoints-1, i) * (1-t)**(numPoints-1-i) * t**i
            pos.x += B * points[i].x
            pos.y += B * points[i].y
        return pos

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