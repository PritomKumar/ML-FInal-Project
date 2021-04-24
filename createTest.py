import  os
import shutil

# basedir = 'F:\\IIT 8th Semester\\Machine Learning\\DataS\\Bnagla Handwritten Letter\\Dataset1 - Copy - Copy'
basedir = 'F:\\IIT 8th Semester\\Machine Learning\\DataS\\Bnagla Handwritten Letter\\Dataset2 - Copy'

for root, dirs, files in os.walk(basedir , topdown=False):
    counter = 0
    print("New folder")
    for name in files:
        if name.endswith("jpg"):
            counter += 1
            if counter>100:
                # print(os.path.join(root, name))
                os.remove(os.path.join(root, name))