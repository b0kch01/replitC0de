# OPEN_ENDED // Nathan Choi // 5/28/2019
# Talked to Kardon, Paul, Marc, Adam

# Asks the user for two inputs, string and number
# Then, prints out a "stacked" string and a boolean in a readable format
# Tried to make this as short as possible to exercise minimalistic programming

def stack_it(input_string):
    return "".join([letter + "\n" for letter in input_string])
def only_3s(input_number):
    return input_number%3==0
def client_code():
    client_num = int(input("Enter an integer: "));client_str = input("Enter something: ");answer = ["Your number is a multiple of 3." if only_3s(client_num) else "Your number is not a multiple of 3.", stack_it(client_str)];print("\nAnswers: \n---------------\n" + answer[0] + "\n" + "Here is your stack: \n\n" + answer[1])

# Check list:
# Starts with comment that has names, group names, today's date = True
# Has a comment that describes what the code does = True
# Has great variable names (ex: input_string, client_num, answer, etc.) = True
# Has a a main method client_code that is called from the console window = True
# Asks and accepts a number and a string from user and stores in variables = True
# Client_code calls two methods with params and prints out "returned" values = True
# stack_it method accepts a string and returns stacked string = True
# only_3s method accepts an integer and returns a boolean = True
