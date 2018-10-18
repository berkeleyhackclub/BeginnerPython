found_letters = []
wrong_letters = []

tries = 5

class answer():
	def __init__(self, word):
		self.word = word

	def __str__(self):
		output = ""
		for let in self.word:
			if let in found_letters:
				output += let
			else:
				output += "_"
		return output

	def has_letter(self, letter):
		for let in self.word:
			if let == letter:
				return True
		return False

	def all_found(self):
		for let in self.word:
			if not let in found_letters:
				return False
		return True

word = answer("coding")

while not word.all_found():
	letter = raw_input("Choose letter: ")
	if letter in wrong_letters or letter in found_letters:
		print("You already guessed that letter.")
	elif word.has_letter(letter):
		print(letter + " is in the word!")
		found_letters.append(letter)
	else:
		print(letter + " is not in the word.")
		tries -= 1
		print("You have " + str(tries) + " left.")
		if tries == 0:
			print("You lose!")
			break
		wrong_letters.append(letter)
	print(word)