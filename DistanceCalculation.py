import math

def calculateDistance(sketch, kmer_length, sketch_percent) :
    common = sketch.getCommon()
    size = sketch.getTotalSizeofSketches()
    return (-1 * math.log((2 * common + .0)/size/sketch_percent))/kmer_length
    #return (-1 * math.log((2 * common + .0)/size))/kmer_length
    
