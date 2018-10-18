found_letters = []
wrong_letters = {}
tries = 5

word = "coding"

def in_word(letter):
	for let in word:
		if let == letter:
			return True
	return False

while True:
	letter = raw_input("Choose letter: ")
	if letter in wrong_letters or letter in found_letters:
		print("You already guessed that letter.")
	elif in_word(letter):
		print(letter + " is in the word!")
		found_letters.append(letter)
	else:
		print(letter + " is not in the word.")
		tries -= 1
		print("You have " + str(tries) + " left.")
		if tries == 0:
			print("You lose!")
			break
		wrong_letters[letter] = True