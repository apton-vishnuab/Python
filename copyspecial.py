import sys
import re
import os
import shutil
import glob
import subprocess

"""Copy Special exercise
"""
def get_path(args):
    n = len(args)
    for i in range(n):
        predir = os.chdir(args[i])
        l=os.listdir(predir)
        for j in l :
            if(re.findall("__.*__", j)):
                print(os.path.abspath(j))
    return



def to_dir(args,dest):
    n = len(args)
    for i in range(n):
        shutil.copy(args[i], dest)
    print("file copyed")
    return



def to_zip(args, dest):
    n= len(args)
    
    os.chdir(dest)
    os.mkdir("test")
    for i in range(n):
        shutil.copy(args[i], dest + "/test")
    shutil.make_archive('test', format = 'zip', root_dir = 'test')
    print("files Ziped")
    return


def main():
  # This basic command-line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
    if args[0] == '--getpath':
        del args[0]
        get_path(args)
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        to_dir(args, todir)
    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        to_zip(args, tozip)
    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

  # +++your code here+++
  # Call your functions
 
if __name__ == "__main__":
    main()