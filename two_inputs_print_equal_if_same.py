# Define a function that would check if the inputs are the same
def equal(first_input,second_input):
    return "equal" if first_input == second_input else "not equal"
# Ask for 2 inputs
first_input = int(input("input 1st number "))
second_input = int(input("input 2nd number "))
#print if the numbers are same or not
print("the two numbers are ",equal(first_input,second_input))