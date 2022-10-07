def match_ends(words):
    count = 0
    # Initalise count as 0 and coming to the loop
    for i in words:
        if(len(i) < 2):         # Skip strings wich have less than two caharacter 
            continue
        if(i[0] == i[-1]):      # If the last character of the string is equal with the first then increiment count by one
            count += 1
    return count



def front_x(words):
    n = len(words)
    words.sort()                # Sort the list words
    words_x = []                # Declare an empty list to store words start with 'x'
    for i in words:
        if(i[0] == 'X' or i[0] == 'x'):     # Add all words start with 'x' to  words_x
            words_x.append(i)
    for i in words_x:
        words.remove(i)                     # Remove all words start with 'x' from the list words
    words_x.extend(words)                   # Add words to words_x
    return words_x



def sort_last(tuples):
    # Normal bubble sort but the change is it will compare last element from each tuple
    for i in range(0, len(tuples) - 1):  
        for j in range(len(tuples) - 1):  
            if(tuples[j][-1] > tuples[j + 1][-1]):  
                temp = tuples[j]  
                tuples[j] = tuples[j + 1]  
                tuples[j + 1] = temp  
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
    test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    
if __name__ == '__main__':
    main()