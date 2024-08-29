#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    if (x < y)
    {
        printf("%i is less than %i\n", x, y);
    }

    else if (x == y)
    {
        printf("%i equals %i\n", x, y);
    }

    else
    {
        printf("%i is greater than %i\n", x, y);
    }
}
