#Create a list comprehension input variable that has 10 inputs
numbers = [int(input("input number "+str(i+1)+":"))for i in range(10)]
first_number = numbers[0]
#use a for loop that starts with the second number to the last number that subtracts itself from the 1st number
for i in numbers[1:]:
    first_number -= i
    result = first_number
#print the statement
print("The result is",result)