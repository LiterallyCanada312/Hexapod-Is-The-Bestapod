#include "Vector.h"
#include <iostream>

using namespace std;

class Bezier{

    public:
    Vector2D getPoint2D(Vector2D* points, float t);

    Vector3D getPoint3D();

    private:

    int interpolate(int from, int to, float percent);

};