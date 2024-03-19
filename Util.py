import Vector

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

def vectorize(arr):
    return Vector.Vector3D(arr[0], arr[1], arr[2])