
# this script prints the endings of the specified lengths and popularity

import os, sys

MIN_LETTERS_IN_ENDING = 8
MAX_LETTERS_IN_ENDING = 10
MIN_ENDING_FREQUENCY = 10

# open file
file_path = sys.argv[1]
file = open(file_path, "r")
lines = file.read().splitlines()

# turn that into a list of words
words = [x.split('\t')[0] for x in lines]

# endings is a dictionary that stores the count of each ending
endings = {}

for n in range(MIN_LETTERS_IN_ENDING, MAX_LETTERS_IN_ENDING + 1):
    
    sys.stderr.write("Processing endings of size: " + str(n) + "\n")
    
    for word in words:
        
        e = word[n - 1:]
        endings[e] = 0
    
    for word in words:

        if len(word) > n:
        
            e = word[n - 1:]
            endings[e] += 1

for k in endings.keys():

    if endings[k] >= MIN_ENDING_FREQUENCY:
    
        print k