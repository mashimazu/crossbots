unsigned int contarBits(unsigned int n)
{
    unsigned int c = 0;
    while (n) {
        c += n & 1;
        n >>= 1;
    }
    return c;
}

