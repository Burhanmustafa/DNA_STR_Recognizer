import sys
from sys import argv, exit
import csv
from csv import reader, DictReader
from itertools import groupby

# If there are not enough arguments then print out the correct usage and exit
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    # Exiting with error
    exit(1)

# Function for skipping to next sequences to avoid counting the same one twice
def skiptonext():
    global t
    t = 0
    while t > 0:
        t -= 1
        continue
    return

# Opening and reading the file with the dna
with open(argv[2]) as txtfile:
    dnareader = reader(txtfile)

    for r in dnareader:
        nucleotides = r


# store the dna in a string
dna = nucleotides[0]

# extract the sequences from the database into a list
with open(argv[1]) as csvfile:
    database = reader(csvfile)

    for r in database:
        sequences = r
        # taking out the name
        sequences.pop(0)
        break

# Creating a dictionary (empty) that will store the different STRs
dict_genes = {}
# The value for each gene will initially be 1 in the dictionary
for i in sequences:
    dict_genes[i] = 1 
    
# Iterating through the dictionary of STRS
for STR in dict_genes:
    global t
    # Setting temporary and temporary MAX to zero at the start of every iteation 
    t = 0
    tM = 0
    length_genes = len(STR)
    length_dna = len(dna)
    
    # Iterating through the length of the DNA
    for i in range(length_dna):
        # Function for skipping to the next sequence
        skiptonext()
        
        # if the length of the segment matches an STR check segments BEFORE to see if the lengths match
        if dna[i: i + length_genes] == STR:
            # While they do, temp is incremented and the iteration skips over to the next one
            while dna[i - length_genes: i] == dna[i: i + length_genes]:
                t += 1
                i += length_genes
            
            # Storing the largest consecutive repeats using temp variables
            if t > tM:
                tM = t
    
    # Ascribing largest consecutive reopeats to its STR
    dict_genes[STR] += tM


# Storing the number of times each STR is repeated in variables
if argv[1] == "databases/large.csv":
    AGATC = dict_genes['AGATC']
    TTTTTTCT = dict_genes['TTTTTTCT']
    AATG = dict_genes['AATG']
    TCTAG = dict_genes['TCTAG']
    GATA = dict_genes['GATA']
    TATC = dict_genes['TATC']
    GAAA = dict_genes['GAAA']
    TCTG = dict_genes['TCTG']
elif argv[1] == "databases/small.csv":
    AGATC = int(dict_genes['AGATC'])
    AATG = dict_genes['AATG']
    TATC = dict_genes['TATC']


with open(argv[1]) as csvfile:
    database = DictReader(csvfile)
    
    # If it is searching from the small database, there are only three STRs
    if argv[1] == "databases/small.csv":
        # Iterating through the csv file
        for person in database:
            people = person
            # If their repeats match the recorded repeats then print their name
            if int(people['AGATC']) == AGATC and int(people['AATG']) == AATG and int(people['TATC']):
                 (people['name'])
    
    elif argv[1] == "databases/large.csv":
        # Iterating through the csv file
        for person in database:
            people = person
            if int(people['AGATC']) == AGATC and int(people['TTTTTTCT']) == TTTTTTCT and int(people['AATG']) == AATG and int(people['TCTAG']) == TCTAG and int(people['GATA']) == GATA and int(people['TATC']) == TATC and int(people['GAAA']) == GAAA:
                print(people['name'])

    # If there is no macth then print "No Match"
    else:
        print("No Match")
            




        
        
        












