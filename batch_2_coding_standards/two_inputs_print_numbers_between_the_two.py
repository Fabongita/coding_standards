#create a function that returns the numbers between the first number and the second number
def between(first_number, second_number):
    if first_number < second_number:
        return range(first_number + 1, second_number)
    else:
        return range(second_number + 1, first_number)
#Initialize two input variables for the 1st and 2nd number
first_number = int(input("Input the first number: "))
second_number = int(input("Input the second number: "))

#print the numbers
print(f"The numbers between {first_number} and {second_number} are:", *list(between(first_number, second_number)))
