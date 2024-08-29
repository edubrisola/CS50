#include <cs50.h>
#include <stdio.h>

int main()
{
    int number = get_int("Put number:\n");
    printf("if %i\n", number);

    if (number != 10)
    {
        printf("%i is different of 10\n", number);
    }
    else 
    {
        printf("%i is equal 10\n", number);
    }
}
