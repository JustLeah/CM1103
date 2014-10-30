def secsToMins(seconds):
	totalMins = seconds // 60
	totalHours = totalMins // 60
	secondsFinal = seconds % 60
	minsFinal = totalMins % 60
	hoursFinal = totalMins // 60
	print("%ih:%im:%is" % (hoursFinal, minsFinal, secondsFinal))

def bitsToSeconds(hours, mins, secs):
	"""
	>>> bitsToSeconds(1, 0, 0)
	3600
	"""
	hoursToSecs = hours * 60 * 60
	minsToSecs = mins * 60
	finalSecs = hoursToSecs + minsToSecs + secs
	return finalSecs
