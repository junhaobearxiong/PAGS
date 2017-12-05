from abc import ABC, abstractmethod

''' Represent both sketches in a single class
    Since the main purpose of creating sketches is to use them to compare the 
    two sequences which generate them, we aim to achieve this purpose with
    minimum overhead. 
    Storing the information of both sketches in one class is more space
    efficient than storing both sketches seperately. '''

class Sketches(ABC) :
    def __init__(self, size) :
        self.maxSize = size # specify the maximum size of a sketch to prevent 
        # accuring too much space
        self.firstSketchSize = 0
        self.currentSize = 0    # keep track of the growing size of a sketch
        self.common = 0 # the number of kmers that are shared by both sketches
        self.firstPass = True   # true indicates that we are processing the
        # first sequence, false indicates the second.
        super().__init__()

    ''' add kmer to the sketches '''
    @abstractmethod
    def addKmer(self, kmer) :
        pass

    ''' print sketches '''
    @abstractmethod
    def printSketches(self):
        pass

    ''' the number of common kmers between both sketches '''
    def getCommon(self) :
        return self.common

    def getSizeOfCurrentSketch(self) :
        return self.currentSize

    ''' tell the sketch we are starting to read the second genome '''
    def endFirstGenome(self, newSize) :
        self.firstPass = False
        self.maxSize = newSize
        self.firstSketchSize = self.currentSize
        self.currentSize = 0

    def getTotalSizeofSketches(self) :
        return self.currentSize + self.firstSketchSize

    

    
    
