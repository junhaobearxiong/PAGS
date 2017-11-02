from Sketch import Sketch


class SimpleSketch(Sketch) :

    def __init__(self, size) :
        self.kmerMap = {}
        self.firstPass = True
        super().__init__()
        
    def addKmer(self, kmer) :

        if (self.currentSize >= self.maxSize) :
            raise ValueError("SketchSize exceeded limit")
        
        if (firstPass) :
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

