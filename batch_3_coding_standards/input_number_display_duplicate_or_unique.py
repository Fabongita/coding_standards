try:
    #initialize a list variable for all of the numbers
    all_numbers = []
    #use a while loop for the input, displaying of "Unique" or "Duplicate"
    while True:
        number_input = int(input("Input a number: " ))
        all_numbers.append(number_input)
        for i in all_numbers:
            if i == number_input:
                if all_numbers.count(i) > 1:
                    print("This number is duplicate :(")
                    break
                else:
                    print("This number is unique :)")
                    break
except ValueError:
    pass