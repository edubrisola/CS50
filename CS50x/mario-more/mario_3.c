#include <stdio.h>
#include <cs50.h>

int main()
{
    int number;
    do
    {
        number = get_int("Height (Positive Numbers): ");
    }
    while (number < 1);

    for (int i = 1; i <= number; i++)
    {
        for (int j = 0; j < number; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
