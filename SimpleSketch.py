from Sketch import Sketch


class SimpleSketch(Sketch) :

    def __init__(self, size) :
        self.kmerMap = {}
        self.firstPass = True
        super().__init__(size)
        
    def addKmer(self, kmer) :
        if (self.currentSize >= self.maxSize) :
            raise ValueError("SketchSize exceeded limit")
       
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

    def endFirstGenome(self, newSize) :
        self.firstPass = False
        self.maxSize = newSize
        self.currentSize = 0

    def printSketch(self):
        count = 0 # the sum of values
        for key, value in self.kmerMap.items():
            count += value
            print('{}: {}'.format(key, value))
        print("The total count of kmers is: {}".format(count))
