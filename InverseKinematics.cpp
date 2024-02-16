#pragma once
#include "InverseKinematics.h"
#include "Constants.h"
#include "Bezier.h"
#include "Vector.h"
#include <Math.h>


using namespace std;

double InverseKinematics::getFemurServoAngle(double x, double y, double z){
    double L = sqrt(y*y + z*z);
    double A = atan(z/y);
    double B = acos((L*L + FEMUR_LENGTH*FEMUR_LENGTH - TIBIA_LENGTH*TIBIA_LENGTH)/(2*L*FEMUR_LENGTH));
    return B + (-A);
};

double InverseKinematics::getTibiaServoAngle(double x, double y, double z){
    double L = sqrt(y*y + z*z);
    return (acos((TIBIA_LENGTH*TIBIA_LENGTH + FEMUR_LENGTH*FEMUR_LENGTH - L*L)/(2*FEMUR_LENGTH*TIBIA_LENGTH)));
};

double InverseKinematics::getCoxaServoAngle(double x, double y){
    
};