float distancia(float p1x,float p1y,float p2x,float p2y)
{
    float d=0;

    d = pow((p2x-p1x),2) + pow((p2y-p1y),2);

    d = sqrt(d);

    d = round(d*100)/100;

    return d;
}

