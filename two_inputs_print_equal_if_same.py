# Define a function that would check if the inputs are the same
def Equal(x,y):
    return "equal" if x == y else "not equal"
# Ask for 2 inputs
x = int(input("input 1st number "))
y = int(input("input 2nd number "))
#print if the numbers are same or not
print("the two numbers are ",Equal(x,y))