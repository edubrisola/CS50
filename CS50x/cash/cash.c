#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;

    int change_owed = get_int("Change Owed: ");

    int coins = 0;

    
    coins += change_owed / quarter;
    change_owed %= quarter;


    coins += change_owed / dime;
    change_owed %= dime;


    coins += change_owed / nickel;
    change_owed %= nickel;


    coins += change_owed;

    printf("%i\n", coins);

    return 0;
}
