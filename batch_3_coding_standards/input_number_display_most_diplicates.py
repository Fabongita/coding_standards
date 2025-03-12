#initialize variables for the list of numbers and the number with the most amount of duplicates
numbers = []
most_duplicates = ()
#Use a while loop to ask for user number inputs which displays the most duplicates if user input is invalid
while True:
    user_input = int(input("input numbers (input non-numbers if you want to stop): "))
    try:
        numbers.append(user_input)
    except ValueError:
        break



