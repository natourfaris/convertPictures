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
        print(width)
        if width == 1920:
            os.rename(imageName,'../Output/Background/' + imageName)
            print(imageName)

        elif height == 1920:
            os.rename(imageName,'../Output/Vertical/' + imageName)
            print(imageName)
        else:
            del im
            os.remove(imageName)

    except FileExistsError:
        print('File {} already exists'.format(imageName))
    except:
        print('File doesn\'t seem to be an image')

    # im = Image.open(imageName)
    # width,height = im.size
    # print(width)
    # if width == 1920:
    #     os.rename(imageName,'../Output/Background/' + imageName)
    #     print(imageName)
    #
    # elif height == 1920:
    #     os.rename(imageName,'../Output/Vertical/' + imageName)
    #     print(imageName)
    # # else:
    # #     os.remove(imageName)
