
#include <stdio.h>
#include <cs50.h>

float medium(int scores[], int n);
int main()
{
    int n = 3;
    int scores[n];

    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score: ");
    }

    float z =  medium(scores, n);
    printf("Medium: %f\n", z);

}

float medium(int scores[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += scores[i];
    }

    return (float)sum / n;
}
