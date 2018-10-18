allPrompts = [ # What were going to be asking
    "How is your day going? ",
    "How do you feel about the rest of the year? "
]

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

for prompt in allPrompts: # Loops through prompts in 'allPrompts'
    userInput = raw_input(prompt) #get input
    userInput = userInput.lower() #make all characters lowercase
    searchInput(userInput) # Always same function call
