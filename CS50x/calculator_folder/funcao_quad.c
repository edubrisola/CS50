#include <cs50.h>
#include <stdio.h>

int function(int a, int t, int u, int v);
int main (void)
{
    int x = get_int("Value of x: ");

    int p = get_int("Coeficient 'a': ");
    int q = get_int("Coeficient 'b': ");
    int r = get_int("Coeficient 'c': ");


    int z = function(x, p, q, r);
    printf("\nThe result is: %i\n\n", z);
}

int function(int a, int t, int u, int v)
{
    int b = (a * a) * t;
    int c = a * u;
    int d = v;

    return b + c + d;
}
