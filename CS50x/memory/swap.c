#include <stdio.h>

void swap(int *a, int *b);
int main(void)
{
    int x = 0;
    int y = 0;

    printf("What is 'x': ");
    scanf("%i", &x);

    printf("What is 'y': ");
    scanf("%i", &y);

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

