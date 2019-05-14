import random
import replit
replit.clear() # Clear the output screen

def get_num():
    print("Enter 4 numbers (spelled out)")
    num_list = []
    for i in range(4):
        num_list.append(input("{}: ".format(i+1))) #https://www.geeksforgeeks.org/python-format-function/ 
        # Replaces {} with i+1
        # It's the same with all the other functions
    return num_list

def get_animal():
    print("Enter 3 animals (plural)")
    animal_list = []
    for i in range(3):
        animal_list.append(input("{}: ".format(i+1)))
    return animal_list

def get_rhyme():
    print("Enter 3 living things that rhyme with hen")
    rhyme_list = []
    for i in range(3):
        rhyme_list.append(input("{}: ".format(i+1)))
    return rhyme_list

def get_things():
    print("Enter 5 things (plural)")
    thing_list = []
    for i in range(5):
        thing_list.append(input("{}: ".format(i+1)))
    return thing_list

def generate_random(all_lists):
    ran_list = []
    for i in range(4):
        ran_list.append(random.choice(all_lists[i]))# For each category, generate a random word. 
    return ran_list

def print_poem(rand): # takes the list of words
    print("-----------------------------")
    print("""An old man exclaimed, "This is weird!--""")
    print("""He said, "It is just as I feared--""")
    print("{} {} and a hen".format(rand[0], rand[1]))
    print("four larks and a {}".format(rand[2]))
    print("Have all made their {} in my beard".format(rand[3]))
    print("-----------------------------")

def main():
    num = get_num()
    animal = get_animal()
    rhyme = get_rhyme()
    things = get_things() # Get the list of answers
    while(True):
        answer = input("Enter any key for another poem or enter q to quit: ") # ask the user
        if answer == "q": break # if someone presses q, the program exits the loop
        rand_list = generate_random([num, animal, rhyme, things]) # Give the lists and run the function that returns a random word from each list and storing it into one big list.
        print_poem(rand_list) # Run the print poem function with the list of random words (chosen from the list of answers ^)

main() # actually run the program ^
replit.clear() # When done, the whole thing clears (optional)
