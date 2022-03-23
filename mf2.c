float *Converter(float horas){
    static float lista[5];

    lista[0] = round(horas/720);
    lista[1] = round(horas/168);

    lista[2] = horas*60;
    lista[3] = lista[2]*60;
    lista[4] = lista[3]*1000;

    return lista;
}

