def teenCase(input_text):
    text = input_text.lower()
    output = ""
    count = 1
    for letter in text:
        if count % 2 == 0:
            letter = letter.upper()
        output += letter
        count += 1
    return output

def ANGRY_INTERNET_COMMENTOR(input_text):
    text =  input_text.upper()
    output = ""
    for letter in text:
        if letter == ",":
            continue
        if letter == ".":
            output += "!!!"
            continue
        if letter == "?":
            output += "??!?!"
            continue
        if letter == "!":
            output += "!!!!!1!!1!"
            continue
        else:
            output += letter
    return output
    
def celebratoryVowels(input_text):
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    counter = 0
    for letter in input_text:
        if letter == "y":
            if input_text[counter + 1] == " ":
                output += letter * 6
                continue
            output += letter
        elif letter in vowels:
            output += letter * 4
        else:
            output += letter
        counter += 1
    return output
        
    
