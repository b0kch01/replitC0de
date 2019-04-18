def caesarShift(text, n):
    output = ""
    for i in range(0, len(text)):
        letter = text[i]
        alphabet = ord(letter.upper()) + n
        if not(alphabet < 65 or alphabet > 90):
            output += chr(alphabet) if letter == letter.upper() else chr(alphabet).lower()
        else:
            output += chr(alphabet - 26) if letter == letter.upper() else chr(alphabet - 26).lower()
    return output
