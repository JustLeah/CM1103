#I couldn't find anything interesting with this code so have an ascii badger called Bruce instead!
#                ___,,___
#           _,-='=- =-  -`"--.__,,.._
#        ,-;// /  - -       -   -= - "=.
#      ,'///    -     -   -   =  - ==-=\`.
#     |/// /  =    `. - =   == - =.=_,,._ `=/|
#    ///    -   -    \  - - = ,ndBRUCEM/\b  \\
#  ,' - / /        / /\ =  - /MM(,,._`YQMML  `|
# <_,=^Kkm / / / / ///H|wnWWdMKKK#""-;. `"0\  |
#        `""QkmmmmmnWMMM\""WHMKKMM\   `--. \> \
#              `""'  `->>>    ``WHMb,.    `-_<@)
#                                `"QMM`.
#                                   `>>>

def doughnuts(n):
	x = n
	#Check if number is 6 or greater
	if n < 6:
		return False
	#See if the number is divisable by 6/9/20
	if n % 6 == 0 or n % 9 == 0 or n % 20 == 0:
		return True
	else:
	#if not true then see if n - 6/9/20 is then divisable by one of the previous ones and keep on decreasing the number until it gets to 0
		while x > 0 and x - 6 > 0:
			x -= 6
			if x % 6 == 0 or x % 9 == 0 or x % 20 == 0:
				return True
		x = n
		while x > 0 and x - 9 > 0:
			x -= 9
			if x % 6 == 0 or x % 9 == 0 or x % 20 == 0:
				return True
		x = n
		while x > 0 and x - 20 > 0:
			x -= 20
			if x % 6 == 0 or x % 9 == 0 or x % 20 == 0:
				return True
		return False

for i in range(1,101):
	if doughnuts(i):
		print('%i is okay!' % i)
	else:
		print('%i is not okay!' % i)
		
		

