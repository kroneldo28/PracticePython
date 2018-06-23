''' Create a program that ask the user a number and then prints out a list of all the divisors of that number. '''

# We ask for an input
print("Give me a number")
num = int(input())

'''We create a list that will contains the divisors 
   in which we add 1 since it's a natural divisor to all number'''
div = [1]

'''We loop through all the numbers from 2 to the number
   to find the divisors and append them to the list '''
for elem in range(2,num):
	if (num % elem) == 0:
		div.append(elem)

''' We append the number itself in the list '''
div.append(num)

''' We print out the list of divisors '''
for elem in div:
	print(elem,"is a divisor of",num)
