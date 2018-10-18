userInput = raw_input("How is your day going? ") #get input
userInput = userInput.lower() #make all characters lowercase

def getResponse(word):
    negativeKeyWords = ["bad","wasn't","not","sucks"]
    positiveKeyWords = ["good","great","awesome","alright","well"]

    if word in negativeKeyWords:
        return "I'm sorry about that."
    elif word in positiveKeyWords:
        return "That's great to hear!"


def searchInput(input):
    listInput = input.split(" ")
    response = "Well, life is life."
    for word in listInput:
        if getResponse(word): #If the word matches our key words
            response = getResponse(word)

    print(response)


searchInput(userInput)
