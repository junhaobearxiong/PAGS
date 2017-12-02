#usr/local/bin
import fileinput as fi
import random
import sys

from SimpleSketches import SimpleSketches
from HashSketches import HashSketches
from DistanceCalculation import calculateDistance

class PAGS:
	def __init__(self):
		''' Attributes '''
		self.kmer_length = 0 # length of a kmer
		self.sketch_percent = 0 # size of the sketch is represents by the percentage of
		# total number of kmers that one wishes to include in the sketch
		# thus skecth_percent is the same for both sketches
		# can interpret this as the probablity of including any particular kmer
		self.take_subseq = 0	# 0 if we are taking substring as kmer, 1 if we are taking subsequence
		self.spaced_length = 0 # spaced length for subsequence
		
		# The maximum size is set to a large value that won't be triggered
		# even if we include every kmer of the genome into the sketch
		# This is because we have not find an appropriate maximum size
		# for the sketch.
		# This will depend on the space constraint when implementing in a larger
		# scale
		self.MAX_SIZE_1 = 9999999999
		self.MAX_SIZE_2 = 9999999999  
		self.total_kmer_count = 0

		# files to test
		self.file_1 = ''
		self.file_2 = ''
		
		''' Tests for different implementations '''
		#self.sketch = HashSketches(self.MAX_SIZE_1)
		#self.sketch = ListSketches(self.MAX_SIZE_1)
		self.sketch = SimpleSketches(self.MAX_SIZE_1)

	''' User Set Parameters '''
	def set_param(self, k, p, ss, sl):
		self.kmer_length = k
		self.sketch_percent = p
		self.take_subseq = ss
		if ss == 1:
			self.spaced_length = sl

	# files is a list of two fasta files to compare
	def compare_genomes(self, files):
		'''
		Compare two genomes and created sketches.
		Args:
			files([str]): a list of two file names. Each file should be the
			fasta file of the genome we wish to compare.
		'''
		# iterate over the command line arguments
		# open each file and process
		for index, arg in enumerate(files):
			print("Currently processing file {}".format(arg))
			with open(arg) as fi:
				temp = '' # used to store the part of the line that doesn't form kmer
				# with the string of the current line
				for i, line in enumerate(fi):
					# preprocessing the input
					line.strip('\n')
					if line[0] == '>':
						continue

					line = temp + line # add the buffer string from the previous line
					# to the beginning of the current line
					
					# either get substring or subsequence as kmer
					if (self.take_subseq == 0):
						temp = self.get_substring(line)
					else:
						temp = self.get_subsequence(line)
			
			# finish processing the first genome
			if (index == 0):
				self.sketch.endFirstGenome(self.MAX_SIZE_2)

	def get_distance(self):
		'''
		Distance calculation
		Return (int) distance
		'''
		dist = calculateDistance(self.sketch, self.kmer_length, self.sketch_percent)
		return dist

	def get_substring(self, line):
		'''
		Helper funcion to get all kmers from a line, randomly selected
		to include them into our sketch
		Args:
			line(str): the line we need to parse
			temp(str): the leftover line that we haven't parsed
		Return:
			temp(str): the part of line that we need to parse
			we return it so we can cancatnate it to the beginning of next
			line
		'''
		# go through each starting position of kmer
		for j in range(0, len(line) - self.kmer_length):
			self.total_kmer_count += 1
			r = random.random() # generate a pseudo random number in [0, 1)
			if (r <= self.sketch_percent):
				# if the random number is within the probablity of
				# including a kmer
				# we add it to our sketch
				kmer = line[j:j+self.kmer_length]  # grab the kmer
				self.sketch.addKmer(kmer)
		temp = line[len(line) - self.kmer_length:]
		return temp


	def get_subsequence(self, line):
		'''
		This helper function extracts subsequences from fasta lines.
		Args:
			line (str): the processed line from the input file.
			total_kmer_count (int): keep track of total kmer count
			spaced_length (int): the gap length between each pair of character in the subsequence

		The script loops through each line and extracts subsequence to store in the hash. The spaced
		length is initialized as 1 so that it will extract consecutive kmers by default. If the 
		coverage string, the substring ranging from the first requested character in the subsequence 
		to the last character, exceeds the length of the line, the function raises an error.
		'''
		chunk_length = self.kmer_length + (self.kmer_length - 1) * self.spaced_length
		if chunk_length > len(line):
			raise ValueError("The subsequence length is too long")
		for j in range(0, len(line) - chunk_length):
			self.total_kmer_count += 1
			r = random.random() # generate a pseudo random number in [0, 1)
			if (r <= self.sketch_percent):
				# if the random number is within the probablity of
				# including a kmer
				# we add it to our sketch
				chunk = line[j:j + chunk_length]
				# attain the subsequence
				subsequence = chunk[::self.spaced_length + 1] 
				self.sketch.addKmer(subsequence)
		temp = line[len(line) - chunk_length:]
		return temp
	
	def print_result(self):
	'''
	Print results when we test our implementation
	'''
		print("Total kmer count of both genomes are {}".format(self.total_kmer_count))
		print("Total # of kmer in common is {}".format(self.sketch.getCommon()))
		print("Total # of kmer in both sketches is {}".format(self.sketch.getTotalSizeofSketches()))
		print("Distance between the two is {}".format(calculateDistance(self.sketch, self.kmer_length, self.sketch_percent)))

