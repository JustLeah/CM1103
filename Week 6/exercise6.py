def stars(m, n):
	counter = 0
	while counter < int(n):
		print('*' * int(m), end="")
		print()
		counter = counter + 1

def randomStuff():
	a = ['tim', 'bob', 'trevor', 'susan', 'anna']
	sorted(a, key=lambda x: (x if x[0] not in ['a', 'e', 'i', 'o' ,'u'] else 'z'))