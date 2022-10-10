import os
import re
import sys
import urllib.request
import webbrowser
import webbrowser
"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    urls = []
    # f = open(filename,'r')
    # text=(f.read())
    # f.close()
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                if (re.search("/puzzle/", word) != None):
                    urls.append(word)
    
    urls = [*set(urls)]
    if(filename == "animal_code.google.com"):
        urls.sort()
    else: 
        urls.sort(key = lambda x: x.split("-")[-1])
        # for i in urls:
        #     print(i)
    return urls
 

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    os.mkdir(dest_dir)
    os.chdir(dest_dir)
    i=1
    lines=["<!DOCTYPE html>\n", "<html>\n", "<body>\n"]
    host = "https://code.google.com"
    for urls in img_urls :
        print("*", end=" ")
        image_url = host+urls
 
        # calling urlretrieve function to get resource
        filenames = "img" + str(i)+".jpg"
        urllib.request.urlretrieve(image_url, filenames)
        lines.append('<img src="%s">'%(filenames,))
        i +=1
    lines.append("</body>\n")
    lines.append("</html>\n")
    f = open("animal.html", "a")
    f.writelines(lines)
    f.close()
    webbrowser.open('file://' + os.path.realpath("animal.html"))
def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)
    
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()

