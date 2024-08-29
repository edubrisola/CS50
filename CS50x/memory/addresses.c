#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = 0;

    printf("Number 'n': ");
    scanf("%i", &n);

    int *p = &n;

    printf("%i\n", n);
    printf("%p\n", &n);
    printf("%i\n", *p);

}
