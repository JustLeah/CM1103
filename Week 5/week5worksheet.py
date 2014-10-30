def secsToMins(seconds):
	totalMins = seconds // 60
	totalHours = totalMins // 60
	secondsFinal = seconds % 60
	minsFinal = totalMins % 60
	hoursFinal = totalMins // 60
	print("%ih:%im:%is" % (hoursFinal, minsFinal, secondsFinal))
