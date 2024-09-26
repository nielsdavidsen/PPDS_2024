strin = 'her er en streng \n'

strin.strip().split()

print(strin)

my_input = ["first line\n", "second line\n", "third line\n"]

def read_input(input_arg):
    for line in my_input:
        print(line.strip())

read_input(my_input[1:])

my_list = list(range(1,5))
for item in enumerate(my_list):
    print(item)

list_of_strings = ['first\n', 'second\n', 'third\n', 'fourth']


list_of_strings = [string.strip() for string in list_of_strings]

print(list_of_strings)