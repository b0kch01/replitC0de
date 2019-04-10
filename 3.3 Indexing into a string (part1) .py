def doubleChar(input_text):
    original_text = input_text
    doubled_text = ""
    for letter in original_text:
        doubled_text += letter * 2
    return doubled_text

def evenLetters(input_text):
    word_list = list(input_text)
    new_word = ""
    for i in range(len(word_list)):
        if i % 2 == 0:
            new_word += word_list[i]
    return new_word
    
def letterCount(input_text, searchLetter):
    searchable_text = input_text
    letter_to_find = searchLetter
    sum = 0
    for letter in searchable_text:
        if letter == letter_to_find:
            sum+=1
    return sum
    
def vowelCount(input_text):
    vowels = ['a','e','i','o','u']
    text = input_text
    count = 0 
    for letter in text:
        if letter in vowels:
            count += 1
    return count
    
def deVowel(input_text):
    vowels = ['a','e','i','o','u']
    text = input_text
    processed_text = ""
    for letter in text:
        if letter not in vowels:
            processed_text += letter
    return processed_text
