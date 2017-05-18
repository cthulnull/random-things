#!/usr/bin/env python
from random import randint as aleatorio

#Select 5 numbers and 2 stars.

#Variables
a = 1
e = 1
# 5 random numbers
print ("The 5 numbers are:")
while (a < 6):
    b = aleatorio(1,50)
    a += 1
    print (b)

# 2 random stars
print ("The 2 stars are:")
while (e < 3):
    h = aleatorio(1,11)
    e += 1
    print (h)
