"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***
import csv
def sumRows(filename, header=False):
	filelist = list()
	filedict = dict()
	with open(filename) as myfile:
		filestuff= csv.reader(myfile, delimiter=',')
		for row in filestuff:
			filelist.append(row)
		if header:
			del filelist[0]
		for i in filelist:
			rowtotal = 0
			for x in range(1, (len(i))):
				if i[x].isdigit():
					rowtotal += float(i[x])
				filedict.update({i[0]: rowtotal})
		return(filedict)
			

def sumColumns(filename):
	filelist = list()
	filedict = dict()
	with open(filename) as myfile:
		filestuff= csv.reader(myfile, delimiter=',')
		for row in filestuff:
			filelist.append(row)
		for x in range(0,len(filelist)):
			coltotal = 0
			for i in range(0, len(filelist[0])):
				if i > 0 and filelist[i][x] != '':
					coltotal += float(filelist[i][x])
				filedict.update({filelist[0][x]: coltotal})
		return(filedict)
				 

