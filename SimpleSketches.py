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
            raise ValueError("Sketches Size exceeded limit")
       
        if (self.firstPass) :
            # add one to the current value, starting from 0 if the key
            # doesn't exist
            self.kmerMap[kmer] = self.kmerMap.get(kmer, 0) + 1
        else :
            if kmer in self.kmerMap :
                # if the first genome has a kmer that occurs only once, while
                # the second genome has one that occurs five times, we only 
                # want to count them as common once. So subtract 1 here. 
                self.kmerMap[kmer] -= 1
                if (self.kmerMap[kmer] == 0) :
                    self.kmerMap.pop(kmer)
                self.common += 1    
        self.currentSize += 1

    def printSketches(self):
        for key, value in self.kmerMap.items():
            print('{}: {}'.format(key, value))
