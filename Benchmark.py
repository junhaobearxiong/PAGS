import sys
from RunTest import run_test
'''
	Pairwise comparison between each pair of genomes as specified in a list of
	FASTA files. Return the distance calculated to a file named "result.txt"
'''


''' Parameters '''
file_list = []
arg_len = len(sys.argv) # length of the argument list
if arg_len < 6:
	print("Not enough command line arguments")
	exit()
sketchType = sys.argv[2] #hash or simple sketch
argumentSpacing = 0 #used to offset the command line arguments
hashType = 0 #number from 0 - 3 to choose hashing type
if (not(sketchType == 'simple' or sketchType == 'hash')) :
        print("Not a valid SketchType: use simple or hash")
        exit()

if (sketchType == 'hash') :
        argumentSpacing = 1
        if arg_len < 7:
                print("Need to provide hash type")
                exit()
        hashType = int(sys.argv[3])
                        
k = int(sys.argv[3 + argumentSpacing])
p = float(sys.argv[4 + argumentSpacing])
ss = int(sys.argv[5 + argumentSpacing])
if ss == 1:
	if arg_len < 7 + argumentSpacing :
		print("Need to provide space length for subsequence")
		exit()
	else:
		sl = int(sys.argv[5 + argumentSpacing])


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
			dist = run_test(duo, sketchType, hashType, k, p, ss, sl=0)
			output = '{} {} {}'.format(x, y, dist)
			print(output, file = f)
		
