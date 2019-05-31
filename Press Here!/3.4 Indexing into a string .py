# The code is searching the list passed it's limit.


def countHi(input_text):
    text = input_text
    count = 0
    for letter in range(len(text)):
        if text[letter] == "h" and text[letter + 1] == "i":
            count += 1
    return count

def countTwoLetters(input_text, substring):
    text = input_text
    search = substring
    count = 0
    for letter in range(len(text)):
        if text[letter] == search[0] and text[letter + 1] == search[1]:
            count += 1
    return count

def catAndDogEquality(input_text):
    dog_count = 0
    cat_count = 0
    text = input_text
    for letter in range(len(text)):
        if text[letter] == "d" and text[letter+1] == "o" and text[letter+2] == "g":
            dog_count += 1
    for letter in range(len(text)):
        if text[letter] == "c" and text[letter+1] == "a" and text[letter+2] == "t":
            cat_count += 1
    return True if cat_count == dog_count else False
    
