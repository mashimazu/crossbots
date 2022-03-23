#include <math.h>

float Conversor(float rad){
    float graus;

    graus = (rad*180)/M_PI;

    graus = round(graus*10)/10;

    return graus;
}
