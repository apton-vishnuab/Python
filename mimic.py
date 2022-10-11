import random
import sys
import re


def mimic_dict(filename):
    dict1 = {}
    """Returns mimic dict mapping each word to list of words which follow it."""
    prev = ''                                       # Set prev as Null
    with open(filename,'r') as f:                   # Open a file with read permission 
        for line in f:                              # fetch the lines from the file
            for word in line.split():               # Seprate words of the line
                
                if (prev in dict1):                 # Update the dictionary value using the key
                    dict1[prev].append(word)
                else:
                    l=[word]
                    dict1.setdefault(prev, l)   # Add a new element to the dictionary with key and value list
                prev=word
    if (prev in dict1):
        dict1[prev].append('')                  # Make a connection bitween first word and last
    else:
        l = ['']
        x = dict1.setdefault(prev, l)           # Make a connection bitween first word and last
    # print(dict1)
    return dict1


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    for i in range(1,201):
        print(i," : ",word)
        word = random.choice(mimic_dict.get(word))
    return


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print ('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()