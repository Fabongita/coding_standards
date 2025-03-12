#initialize a variable for the numbers, and the lowest number to highest
numbers = []
lowest_number_to_highest = None
#use a while loop and try and except for the input
while True:
    input_numbers = input("input a number (input a non-number if you want to stop): ")
    try:
        convert_input_numbers_integer = int(input_numbers)
        numbers.append(input_numbers)
    except ValueError:
        break
#use an if statement to sort through the numbers from highest to lowest and display it
if numbers:
    lowest_number_to_highest = sorted(numbers)
    print(f"the numbers from highest to lowest are:",*lowest_number_to_highest)
else:
    print("no number inputted")
