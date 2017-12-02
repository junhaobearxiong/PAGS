import math

def calculateDistance(sketch, kmer_length, sketch_percent) :
	common = sketch.getCommon()
	if common == 0:
		print("0 common kmers between sketches. Run with smaller k or larger p")
		exit()
	size = sketch.getTotalSizeofSketches()
	return (-1 * math.log((2 * common + .0)/size/sketch_percent))/kmer_length
    #return (-1 * math.log((2 * common + .0)/size))/kmer_length
    
