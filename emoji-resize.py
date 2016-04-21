import glob, os
from PIL import Image
from resizeimage import resizeimage


# Change this to whatever directory your images are in
os.chdir("REPLACE_THIS")


def resize_jpg():
    for file in glob.glob("*.jpg"):
        fd_img = open(file, 'r+b')
        img = Image.open(fd_img)
        img = resizeimage.resize_thumbnail(img, [128, 128])
        name = file.split(".")
        
        # Save them in the directory with the prefix resize
        img.save('resize-' + name[0] +'.jpeg', img.format)
        fd_img.close()


def resize_png():
    for file in glob.glob("*.png"):
        fd_img = open(file, 'r+b')
        img = Image.open(fd_img)
        img = resizeimage.resize_thumbnail(img, [128, 128])
        name = file.split(".")
        # Save them in the directory with the prefix resize

        img.save('resize-' + name[0], img.format)
        fd_img.close()


resize_jpg()
resize_png()
