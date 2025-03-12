#initialize a variable for the numbers, and the lowest number
numbers = []
lowest_number = None
#use a while loop and try and except for the input
while True:
    input_numbers = input("input a number (input a non-number if you want to stop): ")
    try:
        convert_input_numbers_integer = int(input_numbers)
        numbers.append(input_numbers)
    except ValueError:
        break
#use an if statement to determine the lowest number and display it
if numbers:
    lowest_number = min(numbers)
    print(f"the lowest number is",*lowest_number)
else:
    print("there is no number inputted")