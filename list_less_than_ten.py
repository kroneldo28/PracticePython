''' Take a list and print out all the elements of the list that are less than 5 '''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []
for element in a:
	if element < 5:
		b.append(element)

print("Initial list is :",a)
print("Same list with only elements less than 5:",b)

'''  E . x . T . R . A . s '''
''' Ask the user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user '''


print("Initial list is :",a)
print("Type in a number")
num = int(input())
c = []
for element in a:
	if element < num:
		c.append(element)
print("Here's the initial list with only elements less than ",num,":",c)
