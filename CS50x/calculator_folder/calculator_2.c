#include <cs50.h>
#include <stdio.h>

int main(void)
{
    double x = get_double("x: ");
    double y = get_double("y: ");

    double z = (double) x / (double) y;
    printf("%.50f\n", z);
}

