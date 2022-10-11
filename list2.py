def remove_adjacent(nums):
    nums2 = []
    # Here the element on the list num will assigned to nums2 one by one
    for i in nums:
        if(i not in nums2):     # Check the element already in the list
            nums2.append(i)
    return nums2



def linear_merge(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    l1, l2 = 0, 0
    list3 = []
    while(l1 < n1 or l2 < n2):
        if(l1 == n1):                   # It will work if the all elements of the list1 is assigned to list3   
            list3.append(list2[l2])     
            l2 += 1
            continue 
        if(l2 == n2):                   # It will work if the all elements of the list2 is assigned to list3 
            list3.append(list1[l1])
            l1 += 1 
            continue
        if(list1[l1] < list2[l2]):      # It will work if the elements of the list2 is grtater than list1
            list3.append(list1[l1])
            l1 += 1
        else:                           # It will work if the elements of the list1 is grtater than list2
            list3.append(list2[l2])
            l2 += 1
    return list3



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

 
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
                      ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
                      ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
                      ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()