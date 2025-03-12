#initialize variables for input and numbers list
all_numbers_with_duplicates = []
input_numbers = [int(input(f"input numbers {i+1} times : "))for i in range(10)]
#use a for loop to go through the input numbers and determine if it is a duplicate or not
for i in input_numbers:
    if input_numbers.count(i) > 1 and i not in all_numbers_with_duplicates:
        all_numbers_with_duplicates.append(i)
    if input_numbers.count(i) == 1:
        all_numbers_with_duplicates.append(i)
print(f"all of the numbers with duplicates first entry are", *all_numbers_with_duplicates)

