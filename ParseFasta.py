#usr/local/bin
import fileinput as fi
import random

k = 0 # length of a kmer

sketch_percent = 0 # size of the sketch is represents by the percentage of
  # total number of kmers that one wishes to include in the sketch
  # thus skecth_percent is the same for both sketches
  # can interpret this as the probablity of including any particular kmer

sim_sk = SimpleSketch()

k = input('Please specify the length of each k-mer: ')
sketch_percent = input('Please specify the percentage of the total number of '
  'k-mers you wish to include in the sketch: ')
#TODO: exception handling


for i, line in enumerate(fi.input()):
    line.strip('\n')
    for j in range(0, len(line) - k):
    # go through each starting position of kmer
      r = random.random() # generate a pseudo random number in [0, 1)      
      if (r <= p): 
      # if the random number is within the probablity of including a kmer
      # we add it to our sketch
        kmer = line[j:j+k]  # grab the kmer
        sim_sk.addKmer(kmer)
  
