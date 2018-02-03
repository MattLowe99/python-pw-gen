#!/usr/bin/env python3

#Wordlist sampled from http://www.mieliestronk.com/corncob_lowercase.txt

import random
import argparse

parser = argparse.ArgumentParser(description="~~~Generate a password using the XKCD method~~~")
parser.add_argument("-w", "--words", type=int, default=4,
                    help="include WORDS words in the password ")
parser.add_argument("-n", "--numbers", type=int, default=0,
                    help="insert NUMBERS random numbers in the password")
parser.add_argument("-c", "--caps", type=int, default=0,
                    help="capitalize the first letter of CAPS random words")
parser.add_argument("-s", "--symbols", type=int, default=0,
                    help="insert SYMBOLS random symbols in the password")

args = parser.parse_args()

openWordlist = open("XKCDwl.txt")

wordlist = openWordlist.read().splitlines()

wordSubset = random.sample(wordlist, args.words)

capsCount = 0
capsList = []
if (args.caps > 0 and args.caps <= args.words):
    capsSubset = random.sample(wordSubset, args.caps)
    wordSubset = list(set(wordSubset) - set(capsSubset))
    while (capsCount < args.caps):
        capsList.append(capsSubset[capsCount].title())
        capsCount += 1

    wordSubset = wordSubset + capsList
    random.shuffle(wordSubset)

numCount = 0
numList = []
if (args.numbers > 0):
    while (numCount < args.numbers):
        tempList = [str(random.randint(0, 9))]
        numCount += 1
        numList = numList + tempList

    wordSubset = wordSubset + numList
    random.shuffle(wordSubset)

if (args.symbols > 0):
    symList = ["~","!","@","#","$","%","^","&","*",".",":",";"]
    symSubset = random.sample(symList, args.symbols)

    wordSubset = wordSubset + symSubset
    random.shuffle(wordSubset)

password = "".join(wordSubset)
print(password)
