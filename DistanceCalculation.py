import math

def calculateDistance(sketch, kmer) :
    common = sketch.getCommon()
    size = self.getTotalSizeofSketches()
    return (-1 * math.log((2 * common + .0)/size))/kmer
    
