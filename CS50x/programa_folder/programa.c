#include <cs50.h>
#include <stdio.h>

int main()
{
    int x = get_int("What number is x? ");
    int y = get_int("What number is y? ");

    if (x < y)
    {
        printf("%i is less than %i\n", x, y);
    }

    else if (x > y)
    {
        printf("%i is greater than %i\n", x, y);
    }

    else
    {
        printf("%i equals %i", x, y);
    }
}
