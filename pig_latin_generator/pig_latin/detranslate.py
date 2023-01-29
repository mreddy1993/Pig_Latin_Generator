import nltk
nltk.download('words')
from nltk.corpus import words

def detranslate(input_str:str) -> str: 
    """This package will take pig latin words and convert them back to english word"""
    #global output_str
    consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    vowels = ("a","e","i","o","u")

     #logic for converting pig latin to english
    if input_str[len(input_str) - 2:len(input_str)] == "ay":
        if input_str[len(input_str) - 3] in consonants and input_str[len(input_str) - 4] in consonants:
            output_str = input_str[len(input_str) - 4:len(input_str) - 2] + input_str[0:len(input_str) - 4]
            if output_str not in words.words():
               output_str = input_str[len(input_str) - 3] + input_str[0:len(input_str)-3]
        elif input_str[0] in vowels and input_str[len(input_str) - 3] in consonants:
            output_str = input_str[len(input_str) - 3] + input_str[0:len(input_str)-3] 
        elif input_str[len(input_str)-3] == "w":
            output_str = input_str[0:len(input_str) - 3]      
    else:
        output_str = input_str

    return output_str

