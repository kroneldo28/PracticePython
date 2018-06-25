''' Take two lists and write a program that returns a list that contains only the elements 
	that are common between the lists (without duplicate). Make sure the program works 
	on two lists of different sizes. '''

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Let's create our list
res = []

''' We take each element of the first list 
	check if it's also in the second list
	then add it to our res list if it's the case.
	We also check not to add duplicates elements. '''
for elem in a:
	if elem in b and not (elem in res):
		res.append(elem)

print(res)


''' E . X . T . R . A . S  '''

''' Randomly generate two lists to test this '''
randA = random.sample(range(100),30)
randB = random.sample(range(100),30)
randRes=[]
for elem in randA:
	if elem in randB and not (elem in randRes):
		randRes.append(elem)
print(randA)
print(randB)
print(randRes)

''' Write it in one line '''
