#initialize a variable for the numbers, and the highest number
numbers = []
highest_number = None
#use a while loop and try and except for the input
while True:
    input_numbers = input("input a number (input a non-number if you want to stop): ")
    try:
        convert_input_numbers_integer = int(input_numbers)
        numbers.append(input_numbers)
    except ValueError:
        break
#use an if statement to determine the highest number and display it
if numbers:
    highest_number = max(numbers)
    print(f"the highest number is ", *highest_number)
else:
    print("there is no number inputted")