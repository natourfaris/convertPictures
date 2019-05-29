import os
from shutil import copyfile
import sys
from PIL import Image

username = sys.argv[1]

origPath = 'C:\\Users\\{}\\AppData\\Local\\Packages\
\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'\
.format(username)

filenames = os.listdir(origPath)
destination = os.getcwd()

for filename in filenames:
    srcFile = origPath + '\\' + filename
    imageName = filename + '.jpg'
    copyfile(srcFile,destination + '\\' + imageName)
    try:
        im = Image.open(imageName)
        width,height = im.size
        del im
        if width == 1920:
            os.rename(imageName,'../../Output/Background/' + imageName)
            print('Copied {}'.format(imageName[0:10]))

        elif height == 1920:
            os.rename(imageName,'../../Output/Vertical/' + imageName)
            print('Copied {}'.format(imageName[0:10]))
        else:
            os.remove(imageName)

    except FileExistsError:
        print('File {} already exists'.format(imageName[0:10]))
        os.remove(imageName)
    except :
        print('File doesn\'t seem to be an image')
