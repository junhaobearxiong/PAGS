from abc import ABC, abstractmethod

class Sketch(ABC) :
    def __init__(self, size) :
        self.maxSize = size
        self.currentSize = 0
        self.common = 0
        super().__init__()

    @abstractmethod
    def addKmer(self, kmer) :
        pass

    @abstractmethod
    def endFirstGenome(self, newSize) :
        pass

    def getCommon(self) :
        return self.common

    def getSize() :
        return self.size

    

    
    
