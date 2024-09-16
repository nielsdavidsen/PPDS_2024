mylist = [6,9,4,8,7,1,2]

i = 0

while i < len(mylist):
    print(mylist[i])
    i += 1

for i in mylist:
    print(i)

for i, n in enumerate(mylist):
    if i > 0 and n > mylist[i-1]:
        print(n)


#

x = 1

def f(x):
    z = x

for i in range(4):
    x = i
    y = x
    f(x)

print(x)
print(y)
#print(z)

#

def randint():
    return "hello"

import random #overrider ik
from random import randint #overrider
from random import randint as randint2 #overrider ik

print(randint())

