#Harry Riches c1426527
#We will make a function that passes through a 'counter' to figure out the current press 
#as well as passing through  how many presses we want on top of the previous light combination
#I wanted to use recursion here to practice something that we didn't get a chance to do in the lab!
#I also made it so that the user can define the length of the lights, so we can have more then 50 if we want

def swapCh(ch):
	#This function will swap the * to a _ and vice versa
	if ch == '*':
		return '_'
	else:
		return '*'

def xmasLights(totalPresses=50, length=50, currentPress=1, combination=('_'*50)):
	#Our break clause at the top, if the counter is higher then the amount of presses then return the current combination
	#Or if there are no presses just return the current combination
	if (currentPress > totalPresses and currentPress != 1) or totalPresses <= 0:
		return combination
	#Checking to see if the length of the lights is greater than 50 and that none are turned on
	#I wanted to add this in to the function call however I couldn't find a way to do it
	#e.g. def xmasLights(totalPresses=50, counter=1, length=50, combination=('_'*length)):
	#However it kept saying length undefined, which is understandable but sucks at the same time!
	if length > 50 and combination == '_'*50:
		currentPress = currentPress + 1
		return xmasLights(totalPresses, length, currentPress, '*' * length)
	#Set some vars that we need to reset every time this code is run recursivly 
	chCounter = 1
	newcomb = ''
	#Main loop where the magic happens, just cycles through every character depending on how big the lights are
	for chCounter in range(1, length + 1):
	#Swapped from if chCounter % counter == 0 and chCounter != 0: to avoid a division by zero error without adding another condition
		if chCounter != 0 and chCounter % currentPress == 0:
			newcomb = newcomb + swapCh(combination[chCounter - 1])
		else:
			newcomb = newcomb + combination[chCounter - 1]
	currentPress = currentPress + 1
	return xmasLights(totalPresses, length, currentPress, newcomb)

#After 3 presses and after 50
print(xmasLights(3))
print(xmasLights(50))
#Different tests to show it working
#print(xmasLights(-100))
#print(xmasLights(0))
#Used this for debugging to try and figure out the pattern
#for x in range(1,51):
#	print(str(x)[-1], end="")
#print()
#User defined light length
#print(xmasLights(5, 75))
#Print all combinations between 1-50 to see the pattern
#for x in range(1,51):
#	print(xmasLights(x))