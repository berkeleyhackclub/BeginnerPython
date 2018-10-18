def sortWord(letters):
    result = ''
    for letter in letters:
        result = max(letter + result, result + letter)
    print(result)


allWords = ["code","hello","computers","love"]

for word in allWords:
    sortWord(word)
