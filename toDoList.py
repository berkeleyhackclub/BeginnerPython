print("Welcome to your to-do list!")

def printAllInList():
    for item in toDoList:
        print("- " + item)

while True:
    print("")
    print("Press 'a' to add an item, and 'e' to edit your list.")
    print("Your Current List:")
    printAllInList()
    keyChoice = raw_input("Your key: ")
    if keyChoice == "a":
        listItem = raw_input("List item #" + str( len(toDoList) ) + ":")
        toDoList.append(listItem)
    elif keyChoice == "e":
        editIndex = raw_input("Edit index (number):")
        toDoList.remove( toDoList[ int(editIndex) ]  )
