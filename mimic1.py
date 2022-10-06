import random
import sys
import re


def mimic_dict(filename):
    dict1 = {}
    """Returns mimic dict mapping each word to list of words which follow it."""
    prev = ''

    f = open(filename,'r')
    text=(f.read()).split()
    f.close()
    for word in text:
        if (prev in dict1):
            dict1[prev].append(word)
        else:
            l=[word]
            x = dict1.setdefault(prev, l)
        prev=word
    if (prev in dict1):
        dict1[prev].append('')
    else:
        l=['']
        x = dict1.setdefault(prev, l)
    print(dict1)
    return dict1


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    for i in range(1,201):
        print(i," : ",word)
        word=random.choice(mimic_dict.get(word))
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