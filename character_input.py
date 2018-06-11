''' Create a program that asks the user to enter their name and their age.
	Print out a message addressed to them that tells them the year they will turn 100 years old '''

import datetime

print("Hello, what's your name?")
name = input()
print("Nice to meet you "+name+", How old are you please?")
age = int(input())
now = datetime.datetime.now()
forecast = now.year + (100 - age)
print("You'll be 100 years in "+str(forecast)+" "+name+" !")
