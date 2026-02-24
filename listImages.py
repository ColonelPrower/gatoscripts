import os
from PIL import Image

folder = "./"
downloadsFolder = "./done/"

def subdir(subfolder):
    try:
        if os.access(subfolder,os.R_OK) and "/." not in subfolder:
            for filename in os.listdir(subfolder):
                name, extension = os.path.splitext(subfolder+"/"+filename)
                if os.path.isdir(name+extension):
                    subdir(name+extension)
                elif extension in [".jpg",".jpeg",".png"]:
                    print(name+extension)
                    compress(name+extension)
    except OSError as err:
        print(subfolder," dio error, ", err)

def compress(filename):
    picture = Image.open(filename)
    file=filename.split("/")[-1]
    picture.save(downloadsFolder + "compressed_"+file, optimize=True, quality=60)

#if __name__ == "__main__":
for filename in os.listdir(folder):
    name, extension = os.path.splitext(folder+filename)
    subdir(name+extension)
