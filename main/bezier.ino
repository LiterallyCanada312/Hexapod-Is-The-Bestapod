
float factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int getBinomialCoefficient(int n, int k){
    return factorial(n)/(factorial(k) * factorial(n-k));
}

Vector3 getPointOnBezier(Vector3* points[], int n, int t){
    Vector3 target_pos;
    for(int i = 0; i < n; i++){ 
        float b = getBinomialCoefficient((n-1, i) * pow(1 - t, n-1-i)*pow(t, i));
        target_pos.x += b*points[i].x;
        target_pos.y += b*points[i].y;
        target_pos.z += b*points[i].z;
    }

    return target_pos;

}

Vector2 GetPointOnBezierCurve(Vector2* points, int numPoints, float t) {
  Vector2 pos;

  for (int i = 0; i < numPoints; i++) {
    float b = getBinomialCoefficient(numPoints - 1, i) * pow(1 - t, numPoints - 1 - i) * pow(t, i);
    pos.x += b * points[i].x;
    pos.y += b * points[i].y;
  }

  return pos;
  
}