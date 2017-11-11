#usr/local/bin
import fileinput as fi
import random
import sys
from SimpleSketches import SimpleSketches
from DistanceCalculation import calculateDistance

kmer_length = 0 # length of a kmer

sketch_percent = 0 # size of the sketch is represents by the percentage of
  # total number of kmers that one wishes to include in the sketch
  # thus skecth_percent is the same for both sketches
  # can interpret this as the probablity of including any particular kmer

kmer_length = int(input('Please specify the length of each k-mer: '))
sketch_percent = float(input('Please specify the percentage of the total number of '
    'k-mers you wish to include in the sketch: '))
#TODO: exception handling
MAX_SIZE_1 = 9999999999 #TODO: change to dynamic later
MAX_SIZE_2 = 999999999 #TODO: change to dynamic later

sketch = SimpleSketches(MAX_SIZE_1)

# for testing purposes
total_kmer_count = 0

#TODO need to complete kmer that spans multiple line

for index, arg in enumerate(sys.argv[1:]):
    print("Currently processing file {}".format(arg))
    with open(arg) as fi:
        for i, line in enumerate(fi):
            # preprocessing the input
            line.strip('\n')
            if line[0] == '>':
                continue

            for j in range(0, len(line) - kmer_length):
                total_kmer_count += 1
                # go through each starting position of kmer
                r = random.random() # generate a pseudo random number in [0, 1)      
                if (r <= sketch_percent):
                    # if the random number is within the probablity of
                    #including a kmer
                    # we add it to our sketch
                    kmer = line[j:j+kmer_length]  # grab the kmer
                    sketch.addKmer(kmer)
    # finish processing the first genome
    if (index == 0):
        sketch.endFirstGenome(MAX_SIZE_2)



#sketch.printSketches()
print("Total kmer count of both genomes are {}".format(total_kmer_count))
print("Total # of kmer in common is {}".format(sketch.getCommon()))
print("Total # of kmer in both sketches is {}".format(sketch.getTotalSizeofSketches()))
print("Distance between the two is {}".format(calculateDistance(sketch, kmer_length)))  
