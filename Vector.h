struct Vector2D{
    double x;
    double y;

    Vector2D(){}
    Vector2D(double x, double y) : x(x), y(y) {}

    Vector2D& operator+=(const Vector2D& o) {
        x+=o.x; y+=o.y; return *this;
    }
    Vector2D& operator-=(const Vector2D& o){
        x-=o.x; y-=o.y; return *this;
    }
};
Vector2D operator+(Vector2D a, const Vector2D& b) { return a+=b; }
Vector2D operator-(Vector2D a, Vector2D b){ return a-=b; }
Vector2D operator * (float s, Vector2D a){ return Vector2D(s* a.x, s*a.y); }

struct Vector3D{
    double x;
    double y;
    double z;
};
