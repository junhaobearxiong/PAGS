from PAGS import PAGS

''' Run a single test to compare the genomes in two fasta files 
	Return the calculated distance '''
def run_test(k, p, files):
	pags = PAGS()
	pags.set_param(k, p)
	pags.compare_genomes(files)
	dist = pags.get_distance()
	return dist








