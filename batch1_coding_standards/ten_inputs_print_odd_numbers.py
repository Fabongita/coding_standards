#define a function that returns a sum of the odd numbers
def odd(numbers):
    return sum(1 for i in numbers if i % 2 != 0)
#use a list comprehension to input the ten numbers
#display the number of odd numbers