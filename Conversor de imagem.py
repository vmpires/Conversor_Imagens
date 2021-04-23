import os
from PIL import Image

path = os.getcwd()
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jfif' in file:
            files.append(os.path.join(r, file))         

directory = "Convertidos em JPG"  
parent_dir = os.getcwd()
path_pasta = os.path.join(parent_dir, directory)
os.mkdir(path_pasta)

for f in files:
    im = Image.open(f)
    rgb_im = im.convert("RGB")
    f = f.replace('.jfif','')
    splitpath = os.path.split(f)
    splitpath = list(splitpath)
    finalpath = os.path.join(splitpath[0],path_pasta,splitpath[1])
    rgb_im.save(finalpath+".jpg")
    print(f'O arquivo {f} foi convertido para JPG e está na pasta Convertidos em JPG!')

input()