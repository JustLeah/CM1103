from sailing import *
import numpy as np
import matplotlib.pyplot as plt
#####################################################################
#				CALCULATE THE DATA FOR THE GRAPH 					#
#####################################################################

def averagePerformanceScore(numberofraces=6):
	#This function simulates X number of races but instead of returning a list of the winners names it will return a list of 
	#the average performance scores for each the sailors in the race. The point of this is to try and show if it's better to
	#consistent or to have some fluctuation, my prediction is that over all being consistent will be better the larger the number of races 
	
	#Simulates X races and adds the random performance value to a dictionary e.g. 'Alice': [100,100,100,100,100]
	results = {'Alice': [], 'Bob': [], 'Clare': [], 'Dennis': [], 'Eva': []}
	for numbers in range(0, numberofraces):
		curRace = randomPerformance(csvToDict('sailingresults.csv'))
		for name, value in curRace.items():
			results[name].append(value)

	#Goes through each of the races and totals up all of the RPV values and then averages them based on the number of races
	reslist = []
	for name, value in results.items():
		reslist.append([name, value])
		aveRes = [[item[0], sum(item[1])/numberofraces] for item in reslist]

	return sorted(aveRes, key = lambda x: (x[0]))

racestofind = [6, 50, 100, 1000, 10000]
averagePersonScore = {6: [], 50: [], 100: [], 1000: [], 10000: []}

#Iterates through the races that we want to find and runes them all and adds the average RVP values to the racestofind dictionary for each person in 
#Alphabetical order so it's Alice, Bob, Clare, Dennis, Eva

for x in racestofind:
	thisrace = averagePerformanceScore(x)
	for i in thisrace:
		averagePersonScore[x].append(i[1])

#####################################################################
#				FANCY GRAPH WIZADRY GOES ON HERE 					#
#####################################################################

fig, ax = plt.subplots()
n_groups = 5
index = np.arange(n_groups)
bar_width = 0.1
opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, averagePersonScore[6], bar_width,
				alpha=opacity,
				color='b',
				error_kw=error_config,
				label='6 Races')

rects2 = plt.bar(index + bar_width, averagePersonScore[50], bar_width,
				alpha=opacity,
				color='r',
				error_kw=error_config,
				label='50 Races')

rects3 = plt.bar(index + bar_width*2, averagePersonScore[100], bar_width,
				alpha=opacity,
				color='g',
				error_kw=error_config,
				label='100 Races')

rects4 = plt.bar(index + bar_width*3, averagePersonScore[1000], bar_width,
				alpha=opacity,
				color='y',
				error_kw=error_config,
				label='1000 Races')

rects5 = plt.bar(index + bar_width*4, averagePersonScore[10000], bar_width,
				alpha=opacity,
				color='m',
				error_kw=error_config,
				label='10000 Races')

plt.xlabel('Names')
plt.ylabel('Average Random Performance Variable')
plt.title('Mean Random Performance Variable vs Amount of Races')
plt.xticks(index + bar_width*2.5, ('Alice', 'Bob', 'Clare', 'Dennis', 'Eva'))
plt.legend()
plt.tight_layout()
plt.show()