lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
symbols = "!@#$%^&*()-_=+,."
numbers = "12345678"

def check_symbol(input):
    i = 0
    for i in input:
        if i in symbols:
            return 1
    return 0
def check_upper(input):
    i = 0
    for i in input:
        if i in uppercase_letters:
            return 1
    return 0
def check_lower(input):
    i = 0
    for i in input:
        if i in lowercase_letters:
            return 1
    return 0
def check_num(input):
    for i in input:
        if str(i) in numbers:
            return 1
    return 0
            
def password_checker(password):
    if len(password) < 8:
        return "BAD"
    elif check_symbol(password) + check_upper(password) + check_lower(password) + check_num(password) >= 3:
        return "GOOD"
    return "BAD"
