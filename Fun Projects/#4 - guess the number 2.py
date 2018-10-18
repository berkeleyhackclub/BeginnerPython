import random

num = random.randint(1,100)
while True:
	guess = int(raw_input("What is your number? "))

	if guess == num:
		print("You win!")
		break
	elif guess > num:
		print("You guessed to high.")
	elif guess < num:
		print("You guessed to low.")