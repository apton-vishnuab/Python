def verbing(s):
    n=len(s)
    if(n<3):
        return s
    elif(s[-1]=='g' and s[-2]=='n' and s[-3]=='i'):
        return(s+"ly")
    else:
        return(s+"ing")
def not_bad(s):
    posnot=s.find('not')
    posbad=s.find('bad')
    if(posbad>posnot):
        s=s[:(posnot)]+"good"+s[(posbad+3):]
    return s
def front_back(a, b):
    n=len(a)
    m=len(b)
    n1=int((n+1)/2)
    m1=int((m+1)/2)
    res=a[:n1]+b[:m1]+a[n1:]+b[m1:]
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