#include <stdio.h>
#include <string.h>
#include <ctype.h>


typedef struct
{
    int numero;
    char *dia;
}
semana;

int funcao(char *x, char *y);
int main(void)
{

    char a[20];
    char b[20];

    int z = -1;
    int y = -1;

    semana DIA[14];

    DIA[0].numero = 1;
    DIA[0].dia = "domingo";

    DIA[1].numero = 2;
    DIA[1].dia = "segunda";

    DIA[2].numero = 3;
    DIA[2].dia = "terca";

    DIA[3].numero = 4;
    DIA[3].dia = "quarta";

    DIA[4].numero = 5;
    DIA[4].dia = "quinta";

    DIA[5].numero = 6;
    DIA[5].dia = "sexta";

    DIA[6].numero = 7;
    DIA[6].dia = "sabado";

    DIA[7].numero = 8;
    DIA[7].dia = "domingo[2]";

    DIA[8].numero = 9;
    DIA[8].dia = "segunda[2]";

    DIA[9].numero = 10;
    DIA[9].dia = "terca[2]";

    DIA[10].numero = 11;
    DIA[10].dia = "quarta[2]";

    DIA[11].numero = 12;
    DIA[11].dia = "quinta[2]";

    DIA[12].numero = 13;
    DIA[12].dia = "sexta[2]";

    DIA[13].numero = 14;
    DIA[13].dia = "sabado[2]";


    printf("'Insira apenas a primeira palavra, sem acentos' Exemplos: 'Sabado', 'segunda', 'Terca'\n\n");
    printf("'Insira 'dia[2]' para usar os dias da semana seguinte' Exemplos: 'segunda[2]', 'domingo[2]', 'terca[2]'\n\n");
    printf("'Se o valor do 'Dia 1' for maior que o do 'Dia 2', o 'Dia 2' sera representado na proxima semana'\n\n");

    printf("Dia 1: ");
    scanf("%s", a);

    printf("Dia 2: ");
    scanf("%s", b);

    for (int i = 0; i < strlen(a); i++)
    {
        a[i] = tolower(a[i]);
    }

    for (int i = 0; i < strlen(b); i++)
    {
        b[i] = tolower(b[i]);
    }

    for (int i = 0; i < 14; i++)
    {
        if (strcmp(a, DIA[i].dia)== 0)
        {
            z += DIA[i].numero;
            break;

        }
    }

    for (int i = 0; i < 14; i++)
    {
        if (strcmp(b, DIA[i].dia)== 0)
        {
            y += DIA[i].numero;
            break;
        }
    }

    if(strcmp(a, b) == 0)
    {
        y += 7;
    }

    if ((z != -1 && y != -1) && y < z)
    {
        printf("\nResultado: %i\n", (y + 7) - z);
        return 0;
    }

    else if ((z != -1 && y != -1) && y > z)
    {
        printf("\nResultado: %i\n", y - z);
        return 0;
    }

    else
    {
        printf("\nPelo menos um dos dias inseridos nao e valido.\n");
        return 2;
    }

    return 0;

}
