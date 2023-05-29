#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
bool check_valid_key(string s);
//ali em cima, sao todos os librays que eu usei, tudo pode ser encontrando no manual cs50

int main(int argc, string argv[]) //é, ate que nao ta feio, se pa eu pego um 80% nisso, oq ja ta otimo, talvez ate 90%
{
    if (argc != 2 || !check_valid_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int key = atoi(argv[1]); //"13" -> 13

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char c = plaintext [i];
        if (isalpha(c))
        {
            char m = 'A';
            if (islower(c))

               m = 'a';
            printf("%c", (c - m + key) % 26 + m);
        }
        else

               printf("%c", c);

          }
    printf("\n");
}
bool check_valid_key(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
        if (!isdigit(s[i]))
         return false;
         //eu sinceramente nao sei oq eles querem que eu expasse aqui, mas vamo la
     return true;
}
//tá, o algoritmo ta funcionando, e deu pra aprender bastante sobre como funciona o C e como foi feito. é uma troca de palavras, em resumo.