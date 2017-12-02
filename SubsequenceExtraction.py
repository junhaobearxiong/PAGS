def get_subsequence(line, total_kmer_count, temp, spaced_length=0):
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
    chunk_length = kmer_length + (kmer_length - 1) * spaced_length
    if chunk_length > len(line):
        raise ValueError("The subsequence length is too long")
    for j in range(0, len(line) - chunk_length):
                total_kmer_count += 1
                r = random.random() # generate a pseudo random number in [0, 1)
                if (r <= sketch_percent):
                    # if the random number is within the probablity of
                    # including a kmer
                    # we add it to our sketch
                    chunk = line[j:j + chunk_length]
                    # attain the subsequence
                    subsequence = chunk[::spaced_length + 1] 
                    sketch.addKmer(subsequence)
            temp = line[len(line) - chunk_length:]
    return temp
