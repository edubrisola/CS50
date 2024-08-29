#include <stdio.h>
#include <cs50.h>
#include <string.h>

int add(float a, float b);
int subtract(float a, float b);
int mult(float a, float b);
int divide(float a, float b);
int module(int a, int b);

int main()
{
    float x = get_int("x: ");
    string operation = get_string("Operation(add; subtract; mult; divide; module): ");
    float y = get_int("y: ");


    if (strcmp(operation, "add") == 0)
    {
        float z = add(x, y);
        printf("%f\n", z);
    }

    else if (strcmp(operation, "subtract") == 0)
    {
        float i = subtract(x, y);
        printf("%f\n", i);
    }

    else if (strcmp(operation, "mult") == 0)
    {
        float j = mult(x, y);
        printf("%f\n", j);
    }

    else if (strcmp(operation, "divide") == 0)
    {
        float w = divide(x, y);
        printf("%f\n", w);
    }

    else if(strcmp(operation, "module") == 0)
    {
        int c = module(x, y);
        printf("%i\n", c);
    }


}

int add(float a, float b)
{
    return a + b;
}

int subtract(float a, float b)
{
    return a - b;
}

int mult(float a, float b)
{
    return a * b;
}

int divide(float a, float b)
{
    if (b != 0)
    {
        return a / b;
    }
    else
    {
        printf("Error: Division by zero\n");
        return 0;
    }
}



int module(int a, int b)
{
    return a % b;
}
