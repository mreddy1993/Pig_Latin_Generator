def translate(input_str: str) -> str:
    """This Function Converts English to Pig Latin"""
    #Create check lists for consonants and vowels
    consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    vowels = ("a","e","i","o","u")

    #logic for converting english to pig latin
    if input_str[0] in consonants and input_str[1] in vowels:
        output_str = input_str[1:len(input_str)+1] + input_str[0] + "ay"
    elif input_str[0] in consonants and input_str[1] in consonants:
        output_str = input_str[2:len(input_str)+1] + input_str[0] + input_str[1] + "ay"
    elif input_str[0] in vowels:
        output_str = input_str + "way"

    return output_str

