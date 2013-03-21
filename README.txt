
INTRODUCTION
============
Polly is a Python script that generates limericks using a part of speech database and user-defined templates. Read more at http://www.princeton.edu/~saha/polly/

USAGE
=====
1. Download and extract the Part of Speech Database from http://wordlist.sourceforge.net/ and rename the database text file to pos.txt
2. Run "python endings.py pos.txt > endings.txt"
3. Run "python rhymes.py pos.txt endings.txt > rhymes.txt"
4. Run "python polly.py pos.txt rhymes.txt examples/mary.txt"
5. Try replacing the final argument with a limerick template of your own

TEMPLATE FILES
==============
Template files should resemble a limerick, with the words to be generated replaced with 2-character sequences. The first character of each sequence signifies the rhyming group and should be denoted with any of the following: !@#$%^&*. The second character signifies part of speech and should be one of the following:

- N: Noun
- V: Verb
- A: Adjective
- v: Adverb

See the examples/ folder for some example template files.