import random
x = random.random()

if x < 0.5:
    print('Heads')
else:       
    print('Tails')


d = random.random()

for i in range(7):
    if d < i/6:
        print(i)
        break