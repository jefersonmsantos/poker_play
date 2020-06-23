import numpy as np 
import argparse
import imutils
import cv2
from imutils import paths
import os 

ap = argparse.ArgumentParser()
ap.add_argument('-d','--dataset', required=True, help='path to image file')
args = vars(ap.parse_args())


imagePaths = sorted(list(paths.list_images(args["dataset"])))

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    print(imagePath)
    i = 1
    newPath = imagePath.split('.jpg')
    for angle in np.arange(0,360,180):
        rotated = imutils.rotate_bound(image,angle)
        
        cv2.imwrite(newPath[0]+' - '+str(i)+'.jpg',rotated)

        i+=1