
# this scrit generates rhyming limericks according to a provided template

import os, sys, re
from random import randint, choice


MIN_LETTERS_IN_ENDING = 2
MIN_WORDS_TO_LIST = 10

# GENERATE PART OF SPEECH LOOKUP DICTIONARY
file_path = sys.argv[1]
file = open(file_path, "r")
posLookup = {}
for line in file.readlines():

    lineSplit = line.split('\t')
    entry = lineSplit[0]
    try:
        pos = lineSplit[1]
        posLookup[entry] = pos.replace("\n","").replace("|","")
    except:
        print "Failed on " + lineSplit

# LOAD THE RHYMES FILE INTO A LIST OF LISTS
file_path = sys.argv[2]
file = open(file_path, "r")
rhymeGroups = []
for line in file.readlines():
    
    line = line.replace("\n","")
    lineSplit = line.split(',')
    rhymeGroups.append(lineSplit)

# LOAD THE TEMPLATE FILE INTO STRING
file_path = sys.argv[3]
file = open(file_path, "r")
template = file.read()

# READ THE TOKENS INTO LIST
regex = re.compile("(!|@|#|$|%|^|&|\*)(N|V|A|v)")
tokens = re.findall(regex,template)

userWantsMore = True

while userWantsMore:
    
    # output is the final limerick
    output = template

    # this dictionary stores the line of the last rhyme from the same symbol
    runningRhymeDict = {}

    for t in tokens:

        symbol = t[0]
        pos = t[1]

        # determine the index to pull a rhyme from
        if symbol in runningRhymeDict.keys():
            rhymeIndex = runningRhymeDict[symbol]
        else:
            rhymeIndex = randint(0,len(rhymeGroups))

        # keep randomly selecting until POS matches, move on to another rhyme group if tried too many times
        words = rhymeGroups[rhymeIndex]
        word = choice(words)
        tried = 0
        while pos not in posLookup[word]:
            word = choice(words)
            tried += 1

            if tried == 20:
                # change the rhymeIndex! -- DANGER: MIGHT NOT GET SAME RHYME IF SYMBOL ALREADY IN RUNNINGRHYMEDICT
                rhymeIndex = randint(0,len(rhymeGroups))
                words = rhymeGroups[rhymeIndex]
                tried = 0

        # now that we have a word that matches rhyme and POS, add this rhymeIndex to runningRhymeDict for future reference
        runningRhymeDict[symbol] = rhymeIndex

        # now let's replace the first appearance of this token with our newfoundword!
        output = output.replace(symbol + pos, word, 1)

    # PRINT THE FINAL LIMERICK!
    print
    print output
    print 

    # does the user care for more limericks?
    response = raw_input("Care for another limerick? (Say no to stop.) : ").strip().lower()
    if response == "n" or response == "no":
        userWantsMore = False



