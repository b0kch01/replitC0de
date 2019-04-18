def caesarShift(text, n):
    output = ""
    for i in range(0, len(text)):
        output += (chr(ord(text[i].upper()) + n) if text[i] == text[i].upper() else chr(ord(text[i].upper()) + n).lower()) if not((ord(text[i].upper()) + n) < 65 or (ord(text[i].upper()) + n) > 90) else (chr((ord(text[i].upper()) + n) - 26) if text[i] == text[i].upper() else chr((ord(text[i].upper()) + n) - 26).lower())
    return output
