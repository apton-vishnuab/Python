def verbing(s):
    n = len(s)
    # If the length of string is less than 3 return the same string
    if(n < 3):
        return s
    # If the string is end with 'ing' add 'ly' to the string and return it
    elif(s[-1] == 'g' and s[-2] == 'n' and s[-3] == 'i'):
        return(s + "ly")
    # If the string is grater than 3 and not end with 'ing' add 'ing' to the string and return it
    else:
        return(s + "ing")



def not_bad(s):
    posnot = s.find('not')          # Store the position of first occurence of not 
    posbad = s.find('bad')          # Store the position of first occurence of bad
    if(posbad > posnot):
        s = s[ : (posnot)] + "good" + s[(posbad + 3): ]     # Change not to bad sub string to good
    return s



def front_back(a, b):
    n = len(a)
    m = len(b)
    n1 = int((n + 1) / 2)
    m1 = int((m + 1) / 2)
    # Concat a's first half, b's first half, a's second half and b's second half and store it to res
    res = a[ : n1] + b[ :m1] + a[n1: ]+ b[m1: ]
    return res



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


    
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

 
    print ('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()