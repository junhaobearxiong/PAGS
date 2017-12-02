import sys
from RunTest import run_test

''' Parameters '''
file_list = []
k = int(sys.argv[2])
p = float(sys.argv[3])

''' Read file lists '''
# arg is the file containing all the lists of files
with open(sys.argv[1], 'r') as fl:
	for line in fl:
		line = line.rstrip()
		file_list.append(line)

''' Pairwise comparison for files in the list
	Print into a specified file '''
with open ('result.txt', 'w') as f:
	for i, x in enumerate(file_list):
		for j, y in enumerate(file_list):
			if (j <= i):
				continue
			duo = [x, y]
			dist = run_test(k, p, duo)
			output = '{} {} {}'.format(x, y, dist)
			print(output, file = f)
		
