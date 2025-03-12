#initialize a list variable for all of the numbers
all_numbers = []
#use a while loop for the input, displaying of "Unique" or "Duplicate"
while True:
    number_input = (input("Input a number: " ))
    try:
        all_numbers.append(number_input)
        for i in number_input:
            if number_input.count(i) > 1 and i not in all_numbers:
                print("This numbe is unique :)")
            if number_input(i) == 1 and i in all_numbers:
                print("This number is a duplicate :(")
    except ValueError:
        break