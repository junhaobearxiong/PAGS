from Sketches import Sketches
import random
import hashlib


# multiple hash functions
def convert_ascii(kmer):
    output = ''.join(bin(ascii)[2:] for ascii in [ord(char) for char in kmer])
    return output

def binary_hash(kmer):
    answer = 0
    ascii_kmer = convert_ascii(kmer) + '1'
    ascii_kmer += '0'*(20 - (len(ascii_kmer) %20))
    for i in range(int(len(ascii_kmer)/20)):
        char_string = ascii_kmer[20*i:20*(i+1)]
        char_string1, char_string2 = char_string[:10], char_string[10:]
        answer += int(char_string1, 2) ^ int(char_string2, 2)
    return answer

def invert_hash(kmer):
    binary_encoded = convert_ascii(kmer)
    if 'L' in binary_encoded:
        binary_encoded = int(binary_encoded[:-1], 2)
    else:
        binary_encoded = int(binary_encoded, 2)
    temp = 0
    temp = binary_encoded - (binary_encoded << 31)
    binary_encoded = binary_encoded - (temp << 31)
    # Invert with parameter 28
    temp = binary_encoded ^ binary_encoded >> 28
    binary_encoded = binary_encoded ^ temp >> 28
    # Invert with parameter 21
    binary_encoded *= 14933078535860113213
    # Invert with parameter 14
    temp = binary_encoded ^ binary_encoded >> 14
    temp = binary_encoded ^ temp >> 14
    temp = binary_encoded ^ temp >> 14
    binary_encoded = binary_encoded ^ temp >> 14
    # Invert with parameter 265
    binary_encoded *= 15244667743933553977
    # Invert with parameter 24
    temp = binary_encoded ^ binary_encoded >> 24
    binary_encoded = binary_encoded^temp >> 24
    # Invert with 21
    temp = ~binary_encoded
    temp = ~(binary_encoded - (temp << 21))
    temp = ~(binary_encoded - (temp << 21))
    binary_encoded = ~(binary_encoded-(temp << 21))
    return binary_encoded


class HashSketches(Sketches):
    def __init__ (self, size):
        self.kmerMap = {}   # key: kmer, value: number of times it occurs 
        # in the sketch
        super().__init__(size)

    def addKmer(self, kmer, otherHash=0):
        if (self.currentSize >= self.maxSize):
            raise ValueError("SketchesSize exceeded limit")
        if (self.firstPass):    # processing the first sequence
            if otherHash == 0:  # Use Python built-in hash function
                self.kmerMap[hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
            elif otherHash == 1: # Use binary hash function
                self.kmerMap[binary_hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
            elif otherHash == 2: # use sha256 hash function from sha256 function
                hash_sha256 = hashlib.sha256()
                collect_kmer = hash_sha256.update(kmer)
                hash_value = hash_sha256.digest()
                self.kmerMap[hash_value] = self.kmerMap.get(hash(kmer), 0) + 1
            else:
                self.kmerMap[invert_hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
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
