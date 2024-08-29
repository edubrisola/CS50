#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    int t = strlen(s);

    for (int i = 0; i < t; i++)
    {
        if (s[i] >= 'a' &&  s[i] <= 'z')
        {
            if (i == 0)
            {
                printf("After: ");
            }
            printf("%c", s[i] - 32);
        }
        else
        {
            if (i == 0)
            {
                printf("After: ");
            }
            printf("%c", s[i]);
        }
    }
    printf("\n");

}

