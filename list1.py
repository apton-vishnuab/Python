def match_ends(words):
    count=0
    for i in words:
        if(len(i)<2):
            continue
        if(i[0]==i[-1]):
            count+=1
    return count
def front_x(words):
    n=len(words)
    words.sort()
    words_x=[]
    for i in words:
        if(i[0]=='X' or i[0]=='x'):
            words_x.append(i)
    for i in words_x:
        words.remove(i)        
    words_x.extend(words)
    return words_x
def sort_last(tuples):
    for i in range(0,len(tuples)-1):  
        for j in range(len(tuples)-1):  
            if(tuples[j][-1]>tuples[j+1][-1]):  
                temp = tuples[j]  
                tuples[j] = tuples[j+1]  
                tuples[j+1] = temp  
    return tuples
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

 
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
 
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
if __name__ == '__main__':
    main()