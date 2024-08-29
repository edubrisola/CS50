#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Message: ");
    int t = strlen(s);

    printf("Encrypted Message: ");

    for (int i = 0; i < t; i++)
    {

        if (s[i] >= 'a' && s[i] <= 'w')
        {
            printf("%c", s[i] + 3);
        }
        else if (s[i] == 'x')
        {
            printf("a");
        }
        else if (s[i] == 'y')
        {
            printf("b");
        }
        else if (s[i] == 'z')
        {
            printf("c");
        }

        else if (s[i] >= 'A' && s[i] <= 'W')
        {
            printf("%c", s[i] + 3);
        }
        else if (s[i] == 'X')
        {
            printf("A");
        }
        else if (s[i] == 'Y')
        {
            printf("B");
        }
        else if (s[i] == 'Z')
        {
            printf("C");
        }

        else
        {
            printf("%c", s[i]);
        }
    }

    printf("\n");

    return 0;
}

