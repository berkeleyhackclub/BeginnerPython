questions = [
	{
		"question": "Does it have a truck? ",
		"y": "Elephant",
		"n": "Giraffe"
	}
]

while True:
	q = 0
	while True:
		s = raw_input( questions[q]["question"] )
		a = questions[q][s]
		if type(a) == type("123"):
			c = raw_input("Was it " + a + "? ")
			if c == 'y':
				print("YAY")
			else:
				nc = raw_input("What were you thinking about? ")
				nq = raw_input("What is a question? ")
				ny = raw_input("What is the awnser to that question? ")
				questions[q][s] = len(questions)
				questions.append({
					"question": nq,
					"y": ny == 'y' and nc or a,
					"n": ny == 'y' and a or nc
				})
			break
		else:
			q = a