#usr/local/bin
import fileinput as fi
import random
import sys

from SimpleSketches import SimpleSketches
from HashSketches import HashSketches
from DistanceCalculation import calculateDistance
from SubsequenceExtraction import get_subsequence

''' Attributes '''
kmer_length = 0 # length of a kmer
sketch_percent = 0 # size of the sketch is represents by the percentage of
  # total number of kmers that one wishes to include in the sketch
  # thus skecth_percent is the same for both sketches
  # can interpret this as the probablity of including any particular kmer
MAX_SIZE_1 = 9999999999 #TODO: change to dynamic later
MAX_SIZE_2 = 999999999 #TODO: change to dynamic later
# for testing purposes
total_kmer_count = 0

''' Tests for different implementations '''
#sketch = HashSketches(MAX_SIZE_1)
sketch = SimpleSketches(MAX_SIZE_1)

''' User Set Parameters '''
kmer_length = int(input('Please specify the length of each k-mer: '))
spaced_length = int(input('Please specify the spaced length: '))
sketch_percent = float(input('Please specify the percentage of the total number of '
    'k-mers you wish to include in the sketch: '))
#TODO: exception handling
if kmer_length > 80: # when the length of kmer exceeds the length of a line
# reading input becomes hard
    raise ValueError("Kmer length is too long")


#TODO need to complete kmer that spans multiple line
# iterate over the command line arguments
# open each file and process
for index, arg in enumerate(sys.argv[1:]):
    print("Currently processing file {}".format(arg))
    with open(arg) as fi:
        temp = '' # used to store the part of the line that doesn't form kmer
        # with the string of the current line
        for i, line in enumerate(fi):
            # preprocessing the input
            line.strip('\n')
            if line[0] == '>':
                continue

            line = temp + line # add the buffer string from the previous line
            # to the beginning of the current line
            # go through each starting position of kmer
            temp = get_subsequence(line, total_kmer_count, temp, spaced_length=1)
            '''
            for j in range(0, len(line) - kmer_length):
                total_kmer_count += 1
                r = random.random() # generate a pseudo random number in [0, 1)
                if (r <= sketch_percent):
                    # if the random number is within the probablity of
                    # including a kmer
                    # we add it to our sketch
                    kmer = line[j:j+kmer_length]  # grab the kmer
                    sketch.addKmer(kmer)
            temp = line[len(line) - kmer_length:]
            '''
    # finish processing the first genome
    if (index == 0):
        sketch.endFirstGenome(MAX_SIZE_2)



#sketch.printSketches()
print("Total kmer count of both genomes are {}".format(total_kmer_count))
print("Total # of kmer in common is {}".format(sketch.getCommon()))
print("Total # of kmer in both sketches is {}".format(sketch.getTotalSizeofSketches()))
print("Distance between the two is {}".format(calculateDistance(sketch, kmer_length, sketch_percent)))
