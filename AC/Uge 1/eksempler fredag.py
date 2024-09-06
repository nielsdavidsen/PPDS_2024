import random
x = random.random()

if x < 0.5:
    print('Heads')
else:       
    print('Tails')


d = random.random()

for i in range(7):
    if d < i/6:
        print(f"It was a {i}")
        break

my_string = "here is my string it says something about horses"

list_of_words = my_string.split(' ') #splitting at each space, does so as default anyways. You can choose anything as splitter

print(list_of_words)

#finding horses

index = list_of_words.index('horses')
print(index)

sorted = sorted(list_of_words)

print(sorted[:3])