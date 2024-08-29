#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string likeness;
}
person;

int main(void)
{
    person PEOPLE[3];

    PEOPLE[0].name = "Matthieu";
    PEOPLE[0].likeness = "Good";

    PEOPLE[1].name = "Henrique";
    PEOPLE[1].likeness = "Bad";

    PEOPLE[2].name = "Barbara";
    PEOPLE[2].likeness = "Ok";

    string a = get_string("Name: ");

    for (int i = 0; i < 3; i++)
    {
        if (strcmp(a, PEOPLE[i].name) == 0)
        {
            printf("Likeness: %s\n", PEOPLE[i].likeness);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}
