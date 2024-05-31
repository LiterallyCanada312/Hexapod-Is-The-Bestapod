#include "main.ino"
#include "vector.ino"

void calibStand(){
    setLegToVector(1, Vector3(160, 0, 0));
    setLegToVector(2, Vector3(160, 0, 0));
    setLegToVector(3, Vector3(160, 0, 0));
    setLegToVector(4, Vector3(160, 0, 0));
    setLegToVector(5, Vector3(160, 0, 0));
    setLegToVector(6, Vector3(160, 0, 0));

    delay(25);

    moveToPos(1, Vector3(225,0,115));
    moveToPos(2, Vector3(225,0,115));
    moveToPos(3, Vector3(225,0,115));
    moveToPos(4, Vector3(225,0,115));
    moveToPos(5, Vector3(225,0,115));
    moveToPos(6, Vector3(225,0,115));

}