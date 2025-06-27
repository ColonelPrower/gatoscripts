# Imports
import os
import urllib
import urllib.request

# Welcome message
print('Download random stock images from picsum.photos\n(* images download to the current directory)')

# Paths
# get current working directory
cwd = os.getcwd()

# Images
# python 2 uses raw_input() to return a string, python 3 uses input()
imgNum = input('Enter number of images: ')
imgDim = input('Enter image size (e.g. 1920x1080): ').split('x')

# change directory to current working directory
# os.path.join(a,b) if you want to allow custom paths
os.chdir(cwd)


for i in range(1, int(imgNum) + 1):
	i = str(i)
	urllib.request.urlretrieve(('https://picsum.photos/' + imgDim[0] + '/' + imgDim[1] + '?random'), ('stock-image-res-'+imgDim[0]+'x'+imgDim[1]+ '-' + i + '.jpg'))
