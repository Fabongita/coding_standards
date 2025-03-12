#initialize a variable for the numbers
numbers = []
#use a while loop and try and except for the input
while True:
    input_numbers = input("input a number (input a non-number if you want to stop): ")
    try:
        convert_input_numbers_integer = int(input_numbers)
        numbers.append(convert_input_numbers_integer)
    except ValueError:
        break
#use a print function to take the average of all the numbers
print(sum(numbers)/len(numbers))