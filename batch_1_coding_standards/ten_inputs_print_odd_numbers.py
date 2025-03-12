#define a function that returns a sum of the odd numbers
def odd(numbers):
    return sum(1 for i in numbers if i % 2 != 0)
#use a list comprehension to input the ten numbers
numbers = [int(input("input the number "+ str(i+1) +" times:")) for i in range(10)]
#display the number of odd numbers
print("the odd numbers are ", odd(numbers))