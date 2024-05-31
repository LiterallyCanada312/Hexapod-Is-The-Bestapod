#include "vector.ino"


float[] mulMat(float mat1[][], float mat2[][]){
    
    int R1 = sizeof(mat1)/sizeof(float[]); 
    int R2 = sizeof(mat2)/sizeof(float[]);
    int C1 = sizeof(mat1[0])/sizeof(float);
    int C2 = sizeof(mat2[0])/sizeof(float);
    
    float rslt[R1][C2];

    for (int i = 0; i < R1; i++) {
        for (int j = 0; j < C2; j++) {
            rslt[i][j] = 0;
            for (int k = 0; k < R2; k++) {
                rslt[i][j] += mat1[i][k] * mat2[k][j];
            }
        }

    }

    return rslt;

}
