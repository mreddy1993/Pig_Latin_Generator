import nltk
nltk.download('words')
from nltk.corpus import words
#We use NLTKs word list to create a list that will let us check for english words

def sanatize(input_str:str) -> str:
    """This will sanatize all inputs"""
    output_str = input_str.lower();
    consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    vowels = ("a","e","i","o","u")
    for letters in output_str:
        if letters in consonants or letters in vowels or letters == " ":
            pass
        else:
            raise ValueError("Phrase contains nonalphabetic characters")
    if output_str not in words.words():
        raise ValueError("Not an English Word")
    return output_str