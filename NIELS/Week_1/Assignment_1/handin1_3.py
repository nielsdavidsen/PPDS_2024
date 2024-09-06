number_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20\n"

# 1. Cleaning the string of the newline character
number_str_cleaned = number_str.strip('\n')
print(number_str_cleaned)

# 2. Split the string into a list of strings
number_str_list = number_str_cleaned.split(' ')
print(number_str_list)

# 3. Looping through the list and printing
for i in number_str_list:
    print(i)