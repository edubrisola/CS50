#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("phonebook_2.csv", "a");

    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    fprintf(file, "%s: %s\n", name, number);

    fclose(file);
}
