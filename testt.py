import urllib.request
import os
# setting filename and image URL
os.chdir("web")
filename = 'image1'
image_url = "https://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg"
 
# calling urlretrieve function to get resource
urllib.request.urlretrieve(image_url, filename)