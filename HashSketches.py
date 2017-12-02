from Sketches import Sketches

class HashSketches(Sketches):
    def __init__ (self, size):
        self.kmerMap = {}   # key: kmer, value: number of times it occurs 
        # in the sketch
        super().__init__(size)

    def addKmer(self, kmer):
        if (self.currentSize >= self.maxSize):
            raise ValueError("SketchesSize exceeded limit")
       
        if (self.firstPass):    # processing the first sequence
            self.kmerMap[hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
            self.currentSize += 1
        else:   # processing the second sequence
            # if we find a kmer that is already in the map while processing the
            # second sequence, it means that we find a common kmer between both
            # sketches. 
            if hash(kmer) in self.kmerMap:
                self.kmerMap[hash(kmer)] -= 1
                if (self.kmerMap[hash(kmer)] == 0):
                # if a kmer's occurence is down to zero, it means that it has
                # occured in both sketches exactly the same amount of time
                    self.kmerMap.pop(hash(kmer))
                self.common += 1
            self.currentSize += 1
        
    def printSketches(self):
        pass
