import sys

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.



def read_words(filename):
    dict1 = {}
    f = open(filename,'r') 
    text = (f.read()).split()     # Content of the file copy to text as String    
    f.close()
    for word in text:                   # Here we are stored the word as key and count as value of the directory
        if (word in dict1):
            dict1[word] += 1            # It will work if the word is repeted, count will increment
        else:
            dict1.setdefault(word, 1)   # If new word come set new word as key and set count as one
    return dict1



def print_words(filename):
    dict1=read_words(filename)
    sorted_keys = sorted(dict1.keys())                      # It will sort dictinory by key
    sorted_dict = {key:dict1[key] for key in sorted_keys}
    for i in sorted_dict :
        print(i, " : ", sorted_dict.get(i))
    return



def print_top(filename):
    dict1=read_words(filename)
    sort_orders = sorted(dict1.items(), key=lambda x: x[1], reverse=True)   # It will sort dictinory by value in reverse order

    for i in range(20):
        print("{} : {}".format(sort_orders[i][0],sort_orders[i][1]))

        
    return



    
# This basic command line argument parsing code is provided and calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()

