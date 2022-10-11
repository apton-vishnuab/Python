import os
import re
import sys
import urllib.request
import webbrowser



def read_urls(filename):
    urls = []
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if (re.search("/puzzle/", word) != None):
                    urls.append(word)
    
    urls = [*set(urls)]
    if(filename == "animal_code.google.com"):
        urls.sort()
    else: 
        urls.sort(key = lambda x: x.split("-")[-1])
    return urls



def download_images(img_urls, dest_dir):
    os.mkdir(dest_dir)
    os.chdir(dest_dir)
    i = 1
    lines=["<!DOCTYPE html>\n", "<html>\n", "<body>\n"]
    host = "https://code.google.com"
    for urls in img_urls :
        print("*", end=" ")
        image_url = host + urls
 
        # calling urlretrieve function to get resource
        filenames = "img" + str(i) + ".jpg"
        urllib.request.urlretrieve(image_url, filenames)
        lines.append('<img src="%s">'%(filenames, ))
        i += 1
    lines.append("</body>\n")
    lines.append("</html>\n")
    f = open("animal.html", "a")
    f.writelines(lines)
    f.close()
    webbrowser.open('file://' + os.path.realpath("animal.html"))



def main():
    args = sys.argv[1: ]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)
    
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    img_urls = read_urls(todir)

    if todir:
        download_images(img_urls, args[0])
    else:
        print('\n'.join(img_urls))



if __name__ == '__main__':
    main()


