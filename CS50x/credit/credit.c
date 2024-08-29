#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long card_number;

    // Get user input for the credit card number
    do
    {
        card_number = get_long_long("Number: ");
    }
    while (card_number <= 0);

    // Count the number of digits in the card number
    int digit_count = 0;
    long long temp = card_number;
    while (temp > 0)
    {
        temp /= 10;
        digit_count++;
    }

    // Extract the first two digits of the card number
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
        // Perform Luhn's algorithm to validate the card number
        int sum = 0;
        bool multiply = false;
        while (card_number > 0)
        {
            int digit = card_number % 10;
            card_number /= 10;

            if (multiply)
            {
                digit *= 2;
                if (digit > 9)
                {
                    digit = digit % 10 + digit / 10;
                }
            }

            sum += digit;
            multiply = !multiply;
        }

        // Check if the card number is valid
        if (sum % 10 == 0)
        {
            if (digit_count == 15 && (first_two_digits == 34 || first_two_digits == 37))
            {
                printf("AMEX\n");
            }
            else if (digit_count == 16 && (first_two_digits >= 51 && first_two_digits <= 55))
            {
                printf("MASTERCARD\n");
            }
            else if ((digit_count == 13 || digit_count == 16) && first_two_digits / 10 == 4)
            {
                printf("VISA\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}
