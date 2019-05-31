get_words = lambda number, subj, end:[print("Enter {} {} ({})".format(str(number), subj, end)) if i == 0 else input("{}: ".format(i)) for i in range(number+1)];import random;var_list = [get_words(4, "numbers", "spelled out"), get_words(3, "animals", "plural"), get_words(3, "living things that ryhme with hen", "noun"), get_words(5, "things", "plural"), input("Enter any key for another poem or enter q to quit: ")]
while not(var_list[4] == "q" or quit == "q"):quit = input("-----------------------------" + "\nAn old man exclaimed, \"This is weird!--\"" + "\nHe said, \"It is just as I feared--\"" + "\n{} {} and a hen".format(random.choice(var_list[0]), random.choice(var_list[1])) + "\nfour larks and a {}".format(random.choice(var_list[2])) + "\nHave all made their {} in my beard".format(random.choice(var_list[3])) + "\n-----------------------------\nEnter any key for another poem or enter q to quit: ")

# This is the limerick program written in two lines. (while loop must be seperate) 

# I used a lambda function to create a one line function that asks the user for all the words. It's universal so you can call get_words to get whatever you'd like. 

# The use of the semicolon helped, but it did not work the same as other languages so each "line" had to connected in the right order. 
