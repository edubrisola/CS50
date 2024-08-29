#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long long card_number;

    do //Ask the number
    {
        card_number = get_long_long("Number: ");
    }
    while (card_number <= 0);

    //Count the digits
    int digit_count = 0;
    long long temp = card_number;
    while(temp > 0)
    {
        temp /= 10;
        digit_count++;
    }

    //Extract the first two digits of the card number
    long long first_two_digits = card_number;
    while (first_two_digits >= 100)
    {
        first_two_digits /= 10;
    }

    // Check the card type based on the first digits and the number of digits
    if ((digit_count == 15 && (first_two_digits == 34 || first_two_digits == 37)) ||
        (digit_count == 16 && (first_two_digits >= 51 && first_two_digits <= 55)) ||
        ((digit_count == 13 || digit_count == 16) && first_two_digits / 10 == 4))
    {
        //Algorithm
        int sum = 0;

    }
}
