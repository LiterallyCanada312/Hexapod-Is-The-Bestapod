#pragma once
#include "Bezier.h"

Vector2D Bezier::getPoint2D(Vector2D* points, float t){
    Vector2D* temp = new Vector2D();
    memcpy(temp, points, 2 * sizeof(Vector2D));
    int i = 1;
    while(i > 0) {
      for(int k = 0; k < i; k++){
         temp[k] = temp[k] + t * ( temp[k+1] - temp[k]);
         i--;
      }
      Vector2D answer = temp[0];
      delete[] temp;
      return answer;
    }
}

Vector3D Bezier::getPoint3D(){

    
}

 int interpolate(int from, int to, float percent){

    int difference = to-from;
    return from + (difference * percent);

 };
