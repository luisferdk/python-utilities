import os

from PIL import Image  # python3 -m pip install Pillow

originFolder = '{}/original/'.format(os.getcwd())
compressedFolder = '{}/compressed/'.format(os.getcwd())

maxsize = (1500, 1500)

if __name__ == "__main__":
    for filename in os.listdir(originFolder):
        name, extension = os.path.splitext(originFolder + filename)

        if extension in [".jpg", ".jpeg", ".png",".JPG", ".JPEG", ".PNG"]:
            try:
                picture = Image.open(originFolder + filename)
                picture.thumbnail(maxsize)
                picture.save(compressedFolder + filename, optimize=True, quality=60)
                print("Success {}".format(filename))
            except:
                print("Error {}".format(filename))
