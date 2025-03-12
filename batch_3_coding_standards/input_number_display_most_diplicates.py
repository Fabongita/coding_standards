#initialize variables for the list of numbers and the number with the most amount of duplicates
numbers = []
most_duplicates = None
#Use a while loop to ask for user number inputs then stops if it has a valueError
while True:
    user_input = input("input numbers (input non-numbers if you want to stop): ")
    try:
        int_converter = int(user_input)
        numbers.append(int_converter)
    except ValueError:
       break
# An if statement that checks if the number is a duplicate and the most amount of duplicate
if numbers:
    max_count = max(numbers.count(n) for n in numbers)
    most_duplicates = list(set(n for n in numbers if numbers.count(n) == max_count))
    print("Numbers entered:", numbers)
    print("Most duplicated number(s):", most_duplicates)
else:
    print("No numbers were entered.")


