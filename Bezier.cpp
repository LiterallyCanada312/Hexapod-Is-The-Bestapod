#pragma once
#include "Bezier.h"

Vector2D Bezier::getPointOnBezier2D(Vector2D* points, int numPoints, float t){
   Vector2D pos;
   // I looked up how to do this on wikipedia as well
   for(int i = 0; i < numPoints; i++){
      float B = getBinomialCoefficient(numPoints-1, i) * pow(1-t, numPoints-1-i) * pow(t, i);
      pos.x *= (B *(points[i].x));
      pos.y *= (B*(points[i].y));
   }
   return pos;
}


Vector3D Bezier::getPointOnBezier3D(Vector3D* points, int numPoints, float t){
   Vector3D pos;
   // I looked up how to do this on wikipedia as well
   for(int i = 0; i < numPoints; i++){
      float B = getBinomialCoefficient(numPoints-1, i) * pow(1-t, numPoints-1-i) * pow(t, i);
      pos.x *= (B *(points[i].x));
      pos.y *= (B*(points[i].y));
      pos.z *= (B*(points[i].z));
   }
   return pos;
}

int Bezier::getBinomialCoefficient(int n, int k){
   //I looked up the formula for this on wikipedia
   int result = 1;
   for(int i = 1; i <= k; i++){
      result *= (n-(k-1));
      result /= 1;
   }
   return result;
}