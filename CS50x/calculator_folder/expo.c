#include <stdio.h>
#include <cs50.h>
#include <math.h>

int expo(int a, int x);
int main(void)
{
    int coeficiente = get_int("Valor de 'a': ");
    int x = get_int("Valor de 'x': ");

    int z = expo(coeficiente, x);
    printf("Resultado: %i\n", z);
}

int expo(int a, int x)
{
    if (a == 0)
    {
        return 0;
    }

    else if (a > 0)
    {
        if (x == 0)
        {
            return 1;
        }

        else if (x == 1)
        {
            return a;
        }

        else if (x > 0)
        {
            int result = 1;
            for (int i = 0; i < x; i++)
            {
                result *= a;
            }
            return result;
        }

        else
        {
            float result = 1.0;
            for (int i = 0; i > x; i--)
            {
                result /= a;
            }
            return result;
        }
    }

    else 
    {
        if (x == 0)
        {
            return 1;
        }

        else if (x == 1)
        {
            return a;
        }

        else if (x > 0)
        {
            int result = 1;
            for (int i = 0; i < x; i++)
            {
                result *= a;
            }
            return result;
        }

        else
        {
            float result = 1.0;
            for (int i = 0; i > x; i--)
            {
                result /= a;
            }
            return result;
        }
    }
}
