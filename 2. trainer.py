import cv2
import numpy as np
from PIL import Image
import os

path = 'path for dataset folder'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("algorithm file path")

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[0])

        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
            
    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# add "/trainer.yml" at the end of trainer folder path
recognizer.write('trainer folder path /trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces / people trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
