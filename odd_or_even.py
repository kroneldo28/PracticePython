'''Ask the user for a number.Depending on whether the number is even or odd, print out an appropriate message to the user.
	Hint: How does an even/odd number react differently when divided by 2? '''

print("Give me a number!")
number = int(input())

#We check if the number is even or not and print a message
if (number % 2 ) == 0:
	print(number, "is even!")
else:	
	print(number,"is odd!")

''' E . X . T . R . A . S '''

#We check if the number isa multiple of 4
if (number % 4) ==0:
	print(number,"is also a multiple of 4!")

'''Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
	If check divides evenly into num, tell that to the user. If not, print a different appropriate message. '''

print("Give me a first number!")
num = int(input())
print("Give me a second number!")
check = int(input())
if (num % check) == 0:
	print(check,"divides evenly into",num)
