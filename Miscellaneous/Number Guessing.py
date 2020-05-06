import random

randint = random.randint(0, 100)

while True:
	guess = int(input("Guess a number from 0 to 100 >:) "))
	if guess == randint:
		print("Yes! Are you a mindreader!?")
		break;
	elif guess < 0 or guess > 100:
		print("Input out of range")

	elif randint+2 > guess > randint:
		print("So close!")
	elif randint > guess > randint-2:
		print("So close!")

	elif randint+5 > guess > randint:
		print("A litle lower")
	elif randint > guess > randint-5:
		print("A little higher")

	elif randint+10 > guess > randint:
		print("Getting closer...")
	elif randint > guess > randint-10:
		print("Getting closer...")

	elif guess > randint:
		print("No :\'(")
	elif guess < randint:
		print("No :\'(")

	elif guess == 1234:
		print("Nice try...but no")