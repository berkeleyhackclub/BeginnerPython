
global promptData

def getResponse(word, option1KeyWords, option1Resonse, option2KeyWords, option2Response):
    option1Words = option1KeyWords
    option2Words = option2KeyWords

    if word in option1Words:
        return option1Resonse
    elif word in option2Words:
        return option2Response

def searchInput(input, specificPromptData):
    listInput = input.split(" ")
    response = specificPromptData["defaultResponse"]
    for word in listInput:
        possibleResponse = getResponse(word,
        specificPromptData["option1KeyWords"],
        specificPromptData["option1Response"],
        specificPromptData["option2KeyWords"],
        specificPromptData["option2Response"],
        )
        if possibleResponse: #If the word matches our key words
            response = possibleResponse
    print(response)

promptData = [ # What were going to be asking, along with responses
    {
        "prompt":"How is your day going? ",
        "option1KeyWords" : ["good","great","awesome","alright","well"],
        "option1Response" : "That's great to hear!",
        "option2KeyWords" : ["bad","wasn't","not","sucks"],
        "option2Response" : "I am sorry about that :(",
        "defaultResponse" : "Well, life is life I guess."
    },
    {
        "prompt":"What is your favorite color? ",
        "option1KeyWords" : ["blue", "violet", "green", "purple","orange"],
        "option1Response" : "Wow. I love that color too.",
        "option2KeyWords" : ["red","yellow","white","black"],
        "option2Response" : "That color sucks",
        "defaultResponse" : "I don't know that color too well."
    },
    {
        "prompt":"Do you like computer science? ",
        "option1KeyWords" : ["yes", "love", "nice", "cool","awesome", "like"],
        "option1Response" : "Haha I agree. I like it too. ",
        "option2KeyWords" : ["no","not","bad","sucks","annnoying","nope"],
        "option2Response" : "Sorry to hear that. ",
        "defaultResponse" : "Huh?"
    },
]

def initializeProgram(data):
    for specificPromptData in data: # Loops through prompts in 'allPrompts'
        userInput = raw_input(specificPromptData["prompt"]) #get input
        userInput = userInput.lower() #make all characters lowercase
        searchInput(userInput,specificPromptData) # Always same function call

initializeProgram(promptData)
