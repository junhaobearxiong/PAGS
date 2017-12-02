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
		self.MAX_SIZE_1 = 9999999999 #TODO: change to dynamic later
		self.MAX_SIZE_2 = 999999999 #TODO: change to dynamic later
		# for testing purposes
		self.total_kmer_count = 0

		# files to test
		self.file_1 = ''
		self.file_2 = ''
		''' Tests for different implementations '''
		#self.sketch = HashSketches(self.MAX_SIZE_1)
		self.sketch = SimpleSketches(self.MAX_SIZE_1)

	''' User Set Parameters '''
	def set_param(self, k, p):
		'''
		self.kmer_length = int(input('Please specify the length of each k-mer: '))
		self.sketch_percent = float(input('Please specify the percentage of the total number of '
			'k-mers you wish to include in the sketch: '))
		#TODO: exception handling
		if self.kmer_length > 80: # when the length of kmer exceeds the length of a line
		# reading input becomes hard
			raise ValueError("Kmer length is too long")

		'''
		self.kmer_length = k
		self.sketch_percent = p

	# files is a list of two fasta files to compare
	def compare_genomes(self, files):
		#TODO need to complete kmer that spans multiple line
		# iterate over the command line arguments
		# open each file and process
		#for index, arg in enumerate(sys.argv[1:]):
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
					temp = self.get_subsequence(line, temp, spaced_length=1)
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
					'''
			# finish processing the first genome
			if (index == 0):
				self.sketch.endFirstGenome(self.MAX_SIZE_2)

	def get_distance(self):
		dist = calculateDistance(self.sketch, self.kmer_length, self.sketch_percent)
		return dist

	def get_subsequence(self, line, temp, spaced_length=0):
		'''
		This helper function extrcts subsequences from fasta lines.
		Args:
			line (str): the processed line from the input file.
			total_kmer_count (int): keep track of total kmer count
			spaced_length (int): the gap length between each pair of character in the subsequence

		The script loops through each line and extracts subsequence to store in the hash. The spaced
		length is initialized as 1 so that it will extract consecutive kmers by default. If the 
		coverage string, the substring ranging from the first requested character in the subsequence 
		to the last character, exceeds the length of the line, the function raises an error.
		'''
		chunk_length = self.kmer_length + (self.kmer_length - 1) * spaced_length
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
				subsequence = chunk[::spaced_length + 1] 
				self.sketch.addKmer(subsequence)
		temp = line[len(line) - chunk_length:]
		return temp
	
	#sketch.printSketches()
	def print_result(self):
		print("Total kmer count of both genomes are {}".format(self.total_kmer_count))
		print("Total # of kmer in common is {}".format(self.sketch.getCommon()))
		print("Total # of kmer in both sketches is {}".format(self.sketch.getTotalSizeofSketches()))
		print("Distance between the two is {}".format(calculateDistance(self.sketch, self.kmer_length, self.sketch_percent)))

''' Main 
	pags = PAGS()
	pags.set_param()
	pags.compare_genomes()
	pags.print_result()
'''
