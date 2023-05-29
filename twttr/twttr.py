def main():
    #pega a entrada
    message = input("Input: ")
    #remove todas as vogais
    message_without_vowels = shorten(message)
    #imprima "output: "
    print ("Output: " + message_without_vowels)

def shorten(word):
    word_without_vowels = ""
    #loop atraves de cada letra
    for letter in word:
        # checkar se a vogal está colocada em maiusculo ou minusculo
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            #adiciona a letra
            word_without_vowels += letter
        #retorna a palavra
    return word_without_vowels

if __name__ == "__main__":
    main()