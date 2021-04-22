import os
from PIL import Image

def Conversor(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jfif' in file:
                files.append(os.path.join(r, file))         
    for f in files:
        im = Image.open(f)
        rgb_im = im.convert("RGB")
        f = f.replace('.jfif','')
        rgb_im.save(f+".jpg")
        print(f'O arquivo {f} foi convertido para JPG!')


path = os.getcwd()
Conversor(path)
input()