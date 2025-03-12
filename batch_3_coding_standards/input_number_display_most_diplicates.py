#Use a while loop to ask for user number inputs which displays the most duplicates if user input is invalid
while True:
    user_input = int(input("input numbers (input non-numbers if you want to stop): "))
    numbers = []
    numbers.append(user_input)
    most_duplicates = []
    if user_input 