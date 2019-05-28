# OPEN_ENDED // Nathan Choi // 5/28/2019
# Ask the user for two inputs, string and number
# Then, print out a "stacked" string and a boolean.

def stack_it(input_string):
    stacked_string = ""
    for letter in input_string:
        stacked_string += letter + "\n"
    return stacked_string

def only_3s(input_number):
    return True if input_number%3==0 else False

def client_code():
    client_number = input("Give a number: ") # Ask user for a number
    client_string = input("Give some letters: ") # Ask user for some string
    # Error check for correct value types
    try:
        client_number = int(client_number)
    except:
        print("Something went wrong: You didn't give correct numbers :(")
        return
    if client_number == "" or client_string == "":
        print("Something went wrong: You didn't give anything :(")
        return
    # Forming answers
    is_multiple3 = "Your number is not a multiple of 3."
    if only_3s(client_number):
        is_multiple3 = "Your number is a multiple of 3."
    answer_string = stack_it(client_string)
    print("\nAnswers: \n---------------\n" + is_multiple3 + "\n" + "Here is your stack: \n\n" + answer_string)
