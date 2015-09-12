import random
import math

guessTaken = 0

print "Hello, what is your name?"

name = raw_input(">")

number = random.randint(1, 100)
print "Well, " + name + ", I am thinking of a number between 1 and 100"

while guessTaken < 10:
	print "Take a guess"
	guess = int(input(">"))

	guessTaken = guessTaken + 1

	if guess > number:
		print "Your number is too high"
	elif guess < number:
		print "Your number is too low"
	if guess == number:
		break

if guess == number:
	print "Good job!!!"