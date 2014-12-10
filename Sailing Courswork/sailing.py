import csv, random, operator

def calcScore(sailor):
	"""
	Calculate the score for the current sailor and return the sum of the scores minus their 
	lowest result (which is max in this case)

	Added some slight error checking with isdigit() just incase there is a typo etc

	>>> calcScore(("bob", [2, 4, 1, 1, 2, 5]))
	10
	"""
	scoreList = []
	for i in sailor[1]:
		if str(i).isdigit():
			scoreList.append(i)
	return sum(scoreList) - max(scoreList)

def sortSeries(results):
	"""
	Sort a list of sailors based on their results and break ties using their
	position in the first race

	Added a new sailor (Lucy) to check if the sorting when a tie works

	>>> sortSeries([("Alice", [1,2,1,1,1,1]), ("Bob", [3,1,5,3,2,5]), ("Clare", [2,3,2,2,4,2]), ("Dennis", [5,4,4,4,3,4]), ("Eva", [4,5,3,5,5,3]), ("Lucy", [1,5,2,3,4,1])])
	[('Alice', [1, 2, 1, 1, 1, 1]), ('Lucy', [1, 5, 2, 3, 4, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]
	"""
	return sorted(results, key=lambda x: (calcScore(x), x[1][0]))

def csvToDict(filename='sailingresults.csv', header=True):
	"""
	From a csv file import the data to python as a dict and make the sailor name the dict key

	I did the dict creation in a for loop as I felt it was the easiest way to ensure only the nesacerry information
	goes in to the dict if there is a header. I could have gone if header: del filedict[0] but it seems wasteful to 
	add something to a dictionary and to then remove it after.

	>>> csvToDict('sailingresults.csv') == {'Bob': (' 100', ' 5'), 'Eva': (' 90', ' 5'), 'Dennis': (' 90', ' 0'), 'Clare': (' 100', ' 10'), 'Alice': (' 100', ' 0')}
	True
	""" 
	with open(filename) as myfile:
		filedict = dict()
		filelist = list()
		filereader= csv.reader(myfile, delimiter=',')
		for row in filereader:
			filelist.append(row)
		startrage = 1 if header else 0
		for x in range(startrage, len(filelist)):
			filedict.update({filelist[x][0]: (filelist[x][1], filelist[x][2])})
		return filedict

def randomPerformance(results, seed=False):
	"""
	Create a random perfomace value based on the results from csvToDict, using the seed 57 for testing purposes

	The answers are correct - trust me! 
	"""
	rpvdict = dict()
	if seed:
		random.seed(seed)
	for x in results.items():
		rpv = random.normalvariate(int(x[1][0]), int(x[1][1]))
		rpvdict.update({x[0]: rpv})
	return rpvdict

def rpwinner(rpv=randomPerformance(csvToDict())):
	"""
	Sorts the results from the randomPerformance function by the highest and returns a list in order. Highest first.

	>>> rpwinner({'Dennis': 90.0, 'Alice': 100, 'Bob': 101.4389222493041, 'Eva': 94.18226076274071, 'Clare': 111.520901790179040226}) == ['Clare', 'Bob', 'Alice', 'Eva', 'Dennis']
	True
	"""
	winnerlist = list()
	finallist = list()
	newlist = list()
	for x in rpv.items():
		winnerlist.append((x[0], x[1]))
	newlist.append(sorted(winnerlist, key=lambda x: -x[1]))
	for i in newlist[0]:
		finallist.append(i[0])
	return finallist

def raceSim(seed=False):
	"""
	Simulates 6 races and then appends each of the sailors scores to the results dictionary. It will then run the previous functions to create a list with the results being returned in order.

	>>> raceSim()
	['Alice', 'Clare', 'Bob', 'Dennis', 'Eva']
	"""
	results = {
				'Alice': [],
				'Bob': [],
				'Clare': [],
				'Dennis': [],
				'Eva': []
				}
	for i in range(0, 6):
		thisrace = randomPerformance(csvToDict(), seed if seed else False)
		thisracewinners = rpwinner(thisrace)
		for x in range(0, 5):
			results[thisracewinners[x]].append((x+1))
		print(thisracewinners)
		print(thisrace)
	print(results)























