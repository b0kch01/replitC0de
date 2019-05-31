import random as r
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
symbols = "!@#$%^&*()-_=+,."

def generate_password():
    unshuffled = ""
    for i in range(4):
        if i%2==0:
            unshuffled += r.choice(lowercase_letters)
        else:
            unshuffled += r.choice(uppercase_letters)
    for i in range(4):
        if i%2==0:
            unshuffled += str(round(r.random() * 10))
        else:
            unshuffled += r.choice(symbols)
    return "".join(r.sample(unshuffled, 8))
