#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string a = get_string("Word: ");
    int l = strlen(a);

    for (int i = 0; i < l; i++)
    {
        if (a[i] == ' ' || a[i] == '?' || a[i] == '!' || a[i] == '.')
        {
            printf("%c", a[i]);
        }

        else if (a[i] >= 'A' && a[i] <= 'Z')
        {
            printf("%i ", a[i] - 64);
        }

        else if (a[i] >= 'a' && a[i] <= 'z')
        {
            printf("%i ", a[i] - 96);
        }

        else
        {
            printf("%i", a[i]);
        }
    }
    printf("\n");
}

