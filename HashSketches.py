from Sketches import Sketches
import random
import hashlib
import pickle
import numpy
import os


# multiple hash functions
def convert_ascii(kmer):
    """
    This function converts each character in the kmer into 
    binary representation of ascii codes.

    Args:
        kmer (str): kmer string
    Return:
        answer (str): a string composed of binary number  
    """
    output = ''.join(bin(ascii_code)[2:] for ascii_code in [ord(character) for character in kmer])
    return output

def get_primes(start_number, stop_number):
    """
    This function generates a list of prime numbers, and saves to a pickle file.
    Args:
        start_number (int): the lower bound for the list of prime numbers
        stop_number (int): the upper bound for the list of prime numbers
    Return:
        Save the primes list as a pickle object.
    """
    d = {x: True for x in list(range(start_number, stop_number + 1))}
    x = start_number
    while x ** 2 <= stop_number:
        if d[x]:
            y = x ** 2
            while y <= stop_number:
                d[y] = False
                y += x
        x += 1
    l = []
    for x, y in d.items():
        if y:
            l.append(x)
    return l

def binary_hash(kmer, primes):
    """
    This function hashes kmer string into a unique integer value.
    
    Args:
        kmer (str): kmer string
    Return:
        answer (int): integer hash value
    The function first converts the string input into ascii codes in terms of
    binary numbers. Then each binary value will be iterated and used to 
    construct a new hash binary value, with which its first and second halves
    will be XORed to get a integer hash value.
    """
    answer = 0
    ascii_kmer = convert_ascii(kmer) + '1'
    ascii_kmer += '0'*(20 - (len(ascii_kmer) %20))
    for i in range(int(len(ascii_kmer)/20)):
        char_string = ascii_kmer[20*i:20*(i+1)]
        char_string1, char_string2 = char_string[:10], char_string[10:]
        answer += int(char_string1, 2) ^ int(char_string2, 2)
    random_prime = random.choice(primes)
    answer *= random_prime
    return answer

def invert_hash(kmer):
    """
    This function inversely hashes kmer into a binary encoded value withbinary calculation.

    Args:
        kmer (str): input string
    Return:
        binary_encoded (int): binary hash value
    The function is derived from Thomas Peter's integer hashing algorithm. 
    First, each kmer string will be converted to ascii numbers character by character
    through our helper function. Then, it is re-casted to a binary representation
    of integer value, upon which binary conversions are performed in 
    reverse sequence of that in Thomas Peter's hashing algorithm. 
    XOR is involved to gurantee each output to be unique.
    """
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
    # Invert with parameter
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

def hash_function(kmer, which_hash, primes):
    if which_hash == 0:
        return hash(kmer)
    elif which_hash == 1:
        return binary_hash(kmer, primes)
    elif which_hash == 2:
        hash_sha256 = hashlib.sha256()
        collect_kmer = hash_sha256.update(kmer.encode())
        hash_value = hash_sha256.digest()
        return hash_value
    else:
        return invert_hash(kmer)

'''
	Similar implementation of Sketches as SimpleSketches
	But uses hash function to store the kmers in the sketches
'''


class HashSketches(Sketches):
    def __init__ (self, size, hashFunction = 1):
        self.otherHash = hashFunction 
        self.kmerMap = {}   # key: kmer, value: number of times it occurs
                            #in the sketch
        self.primes = get_primes(2, 50000)
        super().__init__(size)

    def addKmer(self, kmer):
        if (self.currentSize >= self.maxSize):
            raise ValueError("SketchesSize exceeded limit")
        if (self.firstPass):    # processing the first sequence
            '''
            if self.otherHash == 0:  # Use Python built-in hash function
                self.kmerMap[hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
            elif self.otherHash == 1: # Use binary hash function
                self.kmerMap[binary_hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
            elif self.otherHash == 2: # use sha256 hash function from sha256 function
                hash_sha256 = hashlib.sha256()
                collect_kmer = hash_sha256.update(kmer)
                hash_value = hash_sha256.digest()
                self.kmerMap[hash_value] = self.kmerMap.get(hash(kmer), 0) + 1
            else:
                self.kmerMap[invert_hash(kmer)] = self.kmerMap.get(hash(kmer), 0) + 1
            '''
            self.kmerMap[hash_function(kmer, self.otherHash, self.primes)] = self.kmerMap.get(hash_function(kmer, self.otherHash, self.primes), 0) + 1
            self.currentSize += 1
        else:   # processing the second sequence
            # if we find a kmer that is already in the map while processing the
            # second sequence, it means that we find a common kmer between both
            # sketches.
            if hash_function(kmer, self.otherHash, self.primes) in self.kmerMap:
                self.kmerMap[hash_function(kmer, self.otherHash, self.primes)] -= 1
                if (self.kmerMap[hash_function(kmer, self.otherHash, self.primes)] == 0):
                # if a kmer's occurence is down to zero, it means that it has
                # occured in both sketches exactly the same amount of time
                    self.kmerMap.pop(hash_function(kmer, self.otherHash, self.primes))
                self.common += 1
            '''
            if hash(kmer) in self.kmerMap:
                self.kmerMap[hash(kmer)] -= 1
                if (self.kmerMap[hash(kmer)] == 0):
                # if a kmer's occurence is down to zero, it means that it has
                # occured in both sketches exactly the same amount of time
                    self.kmerMap.pop(hash(kmer))
                self.common += 1
            '''
            self.currentSize += 1
        
    def printSketches(self):
        pass
