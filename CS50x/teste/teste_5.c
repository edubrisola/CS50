#include <stdio.h>
#include <string.h>

int main()
{
    char nomes[3][10] = {"Carter", "David", "John"};
    char nome[10] = {0};

    printf("Name: ");
    scanf("%s", nome);

    for (int i = 0; i < 3; i++)
    {
        if (strcmp(nome, nomes[i]) == 0)
        {
            printf("Name Found\n");
            return 0;
        }
    }

    printf("Name Not Found\n");
    return 1;
}
