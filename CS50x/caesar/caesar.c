#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

bool only_digits(string s);

char rotate(char c, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        printf("%c", rotate(plaintext[i], key));
    }
    printf("\n");

    return 0;
}

bool only_digits(string s)
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int key)
{
    if (islower(c))
    {
        return 'a' + (c - 'a' + key) % 26;
    }
    else if (isupper(c))
    {
        return 'A' + (c - 'A' + key) % 26;
    }
    else
    {
        return c;
    }
}
