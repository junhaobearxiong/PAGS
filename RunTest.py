from PAGS import PAGS

''' Run a single test to compare the genomes in two fasta files 
	Args: ss(int): 0 if we are taking substring, 1 if we are taking subsequence
		sl(int): spaced length for subsequence
	Return the calculated distance between the two genomes
'''

def run_test(files, sketchType, hashType, k, p, ss, sl):
	pags = PAGS()
	pags.set_param(sketchType, hashType, k, p, ss, sl)
	pags.compare_genomes(files)
	dist = pags.get_distance()
	return dist








