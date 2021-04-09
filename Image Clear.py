from PIL import Image
import os 

def imageChangeFuction(path):
    try:
        im = Image.open(path)
        pixelMap = im.load()
        
        img = Image.new( im.mode, im.size)
        pixelsNew = img.load()
        
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixelMap[i,j]>(90,90,90,255):
                    # pixelMap[i,j] = (255,255,255,255)
                    pixelsNew[i,j] = (255,255,255,255)
                if pixelMap[i,j]<(90,90,90,255):
                    # pixelMap[i,j] = (0,0,0,255)
                    pixelsNew[i,j] = (0,0,0,255)

                # if pixelMap[i,j]>(254,254,254,255):
                #     pixelsNew[i,j] = (0,0,0,255)

                # if pixelMap[i,j]<(1,1,1,255):
                #     pixelsNew[i,j] = (255,255,255,255)
            
        im.close()
        #img.show()       
        img.save(path) 
        img.close()
        print(path)
    except:
        print("Remove path = " + path)
        os.remove(path)

def imageResize(path):
    try: 
        base = 100
        img = Image.open(path)
        # wpercent = (basewidth/float(img.size[0]))
        # hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((base,base), Image.ANTIALIAS)
        img.save(path)
        print(path)
    except:
        print("Remove path = " + path)
        os.remove(path)

# path = "F:\\IIT 8th Semester\\Machine Learning\\DataS\\Bnagla Handwritten Letter\\Bangla handwritten Letter\\BasicFinalDatabase100\\Train"
path = "F:\\IIT 8th Semester\\Machine Learning\\DataS\\Bnagla Handwritten Letter\\Bangla handwritten Letter\\BasicFinalDatabase"

for root, dirs, files in os.walk(path):
    for f in files:
        filePath = os.path.join(root, f)
        # print(filePath)
        imageResize(filePath)
        imageChangeFuction(filePath)

