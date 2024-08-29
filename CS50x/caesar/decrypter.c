#include <stdio.h>
#include <cs50.h>
#include <string.h>

string decrypt(string a);
int main()
{
    string enigma = get_string("Decrypt: ");

    printf("Decrypted: ");
    string z = decrypt(enigma);
}

string decrypt(string a)
{
    int t = strlen(a);

    for (int i = 0; i < t; i++)
    {

        if (a[i] >= 'd' && a[i] <= 'z')
        {
            printf("%c", a[i] - 3);
        }
        else if (a[i] == 'c')
        {
            printf("z");
        }
        else if (a[i] == 'b')
        {
            printf("y");
        }
        else if (a[i] == 'a')
        {
            printf("x");
        }

        else if (a[i] >= 'D' && a[i] <= 'Z')
        {
            printf("%c", a[i] - 3);
        }
        else if (a[i] == 'C')
        {
            printf("Z");
        }
        else if (a[i] == 'B')
        {
            printf("Y");
        }
        else if (a[i] == 'A')
        {
            printf("X");
        }

        else
        {
            printf("%c", a[i]);
        }
    }

    printf("\n");

    return 0;
}
