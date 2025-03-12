#define a function that returns the bigger number
def checker(first_number, second_number):
    return first_number if first_number > second_number else second_number
#ask for 2 inputs
first_number = int(input("input the first number: "))
second_number = int(input("input the second number: "))
#prints the function
print("bigger number is", checker(first_number,second_number))
