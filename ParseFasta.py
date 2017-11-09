#usr/local/bin
import fileinput as fi
import random
from SimpleSketch import SimpleSketch

k = 0 # length of a kmer

sketch_percent = 0 # size of the sketch is represents by the percentage of
  # total number of kmers that one wishes to include in the sketch
  # thus skecth_percent is the same for both sketches
  # can interpret this as the probablity of including any particular kmer


k = int(input('Please specify the length of each k-mer: '))
sketch_percent = float(input('Please specify the percentage of the total number of '
    'k-mers you wish to include in the sketch: '))
#TODO: exception handling
MAX_SIZE_1 = 100 #TODO: change to dynamic later
MAX_SIZE_2 = 200 #TODO: change to dynamic later

sim_sk = SimpleSketch(MAX_SIZE_1)

# for testing purposes
total_kmer_count = 0


#TODO need to complete kmer that spans multiple lines 
for i, line in enumerate(fi.input()):
    # preprocessing the input
    line.strip('\n')
    if line[0] == '>':
        continue
    
    for j in range(0, len(line) - k):
        total_kmer_count += 1

    # go through each starting position of kmer
        r = random.random() # generate a pseudo random number in [0, 1)      
        if (r <= sketch_percent): 
        # if the random number is within the probablity of including a kmer
        # we add it to our sketch
            kmer = line[j:j+k]  # grab the kmer
            sim_sk.addKmer(kmer)


sim_sk.endFirstGenome(MAX_SIZE_2)
sim_sk.printSketch()
print("Total kmer count is: {}".format(total_kmer_count))


  
