from Sketches import Sketches
from random import random


class MakeSketches(Sketches):
    def __init__(self, size):
    	self.kmerMap = {}
        self.firstPass = True
        super().__init__()
    
    def addKmer(self, kmer):
        pass
    
    def endFirstGenome(self, newSize):
    	pass

'''
    Use ParseFasta.py to parse file and generate kmers.
    # generate bags of k-mers for both genomes
    def generate_kmers(genome, kmer_size):
        kmers = 
        for i in range(len(genome) - kmer_size + 1):
            kmers.add(genome[i:i + kmer_size])
        return kmers
'''

    def get_minhash(k_mers, sketch_size, random_substrings):
        minhash_sketch = []
        minhash = sys.maxint # use collocation counters instead to return n number of lowest words
        for i in range(sketch_size):
            for kmer in k_mers:
                hash_candidate = abs(hash(kmer + random_substrings[i])) # make each hash value unique 

                if hash_candidate < minhash:
                    minhash = hash_candidate
            minhash_sketch.append(minhash)
        return minhash_sketch

    # function for getting sketches
    def get_similar_docs(genome, sketch_size=200, kmer_size=3):
        hash_bands = {}
        random_substrings = [str(random.random()) for _ in range(sketch_size)]
        k_mers = generate_kmers(genome, shingle_size)
        minhash_sketch = get_minhash(k_mers, sketch_size, random_substrings)
        return minhash_sketch
