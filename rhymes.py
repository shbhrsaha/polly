
# this script takes a list of endings and prints the words, one ending on each line for all the words that match

import os, sys

# reinforces the parameter in endings.py
MIN_WORDS = 10

# turn POS into words list
file_path = sys.argv[1]
file = open(file_path, "r")
lines = file.read().splitlines()
words = [x.split('\t')[0] for x in lines]

# turn ENDINGS into endings list
file_path = sys.argv[2]
file = open(file_path, "r")
lines = file.read().splitlines()
endings = [x.replace("\n","") for x in lines]

for ending in endings:
    
    collected = []
    
    for word in words:

        length = len(ending)
        if word[length - 1:] == ending:
            collected.append(word)

    if len(collected) >= MIN_WORDS:
        print ",".join(collected)