#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main()
{
    person people[3];

    people[0].name = "Eduardo";
    people[0].number = "45 99822-0343";

    people[1].name = "Vinicius";
    people[1].number = "45 99946-4968";

    people[2].name = "Anna";
    people[2].number = "45 99911-0053";

    string a = get_string("Name: ");

    for (int i = 0; i < 3; i++)
    {
        if(strcmp(a, people[i].name) == 0)
        {
            printf("Phone Number: %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}
