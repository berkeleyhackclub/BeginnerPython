
### DONT COMPILE THIS PAGE FOR REFERENCE ONLY.
# PRIMITIVE TYPES:
ageInteger = 21 # integer
ageFloat = 21.0 # float
name = "Greg" # string
nameIsString = True # boolean

# ARRAYS:
allClasses = ["History", "Math" ] # 0, 1, 2 ect...
allClasses.append("English")
allClasses[0] = "Computer Science"

# FOR LOOPS:
for arrayObject in allClasses:
    print(arrayObject)

# WHILE LOOPS:
condition = True
while condition:
    print("The condition is true, this loop will last forever.")

# IF ELSE STATEMENTS:
naftaliAge = 12

if naftaliAge < 18:
    print("Naftali is only " + str(naftaliAge) + " and not old enought to drink")
else:
    print("Naftali is old enough to drink")
    # do something else


# FUNCTIONS
def oldEnoughToVote(name, age):
    if age < 18:
        print(name + " is only " + str(age) + " and cannot vote"  )
    else:
        print(name + " can vote!")

oldEnoughToVote("Mr. Albinson", 28) #call function
