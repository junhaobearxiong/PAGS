from Sketches import Sketches

'''
    A simple implementation of Sketches
    Store the kmer and the number of time it occurs in a dict
''' 

class SimpleSketches(Sketches) :

    def __init__(self, size) :
        self.kmerMap = {}
        super().__init__(size)
        
    def addKmer(self, kmer) :
        if (self.currentSize >= self.maxSize) :
            raise ValueError("SketchesSize exceeded limit")
       
        if (self.firstPass) :
            # add one to the current value, starting from 0 if the key
            # doesn't exist
            self.kmerMap[kmer] = self.kmerMap.get(kmer, 0) + 1
            self.currentSize += 1
        else :
            if kmer in self.kmerMap :
                self.kmerMap[kmer] -= 1
                if (self.kmerMap[kmer] == 0) :
                    self.kmerMap.pop(kmer)
                self.common += 1
            self.currentSize += 1

    def printSketches(self):
        count = 0 # the sum of values
        for key, value in self.kmerMap.items():
            count += value
            print('{}: {}'.format(key, value))
        print("The total count of kmers is: {}".format(count))
