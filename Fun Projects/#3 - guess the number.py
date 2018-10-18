num = 17
while True:
	guess = int(raw_input("What is your number? "))

	if guess == num:
		print("You win!")
		break
	else:
		print("You lose")