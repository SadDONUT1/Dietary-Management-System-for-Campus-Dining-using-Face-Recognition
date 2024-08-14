import cv2
import numpy as np
import os 
import socket
import requests
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
#trainer path
recognizer.read('trainer.yml path')

#haarcascade path 
cascadePath = "algorithm file path"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_TRIPLEX 

final_food_info = [['Jaamcian Pasta', ['']], ['Beef Vindaloo', ['5', '6', '16']], ['Garlic Bread', ['1', '5', '6', '13']], ['Cauliflower with Peas', ['1', '2', '5', '6', '8', '9', '13', '15', '16', '18']], ['Vage Dalcha', ['9', '13']], ['Indian Long Beans', ['1', '2', '5', '']]]

HOST = 'your current ip address' #ifconfig / ipconfig
# Enter IP or Hostname of your server
PORT = 20000
# Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))


final_food_info = str(final_food_info)
final_food_info = final_food_info.encode()

s.send(final_food_info)


#iniciate id counter
id = 0
# names related to id
names = ["None", "12345", "12346"]

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 3024) # set video widht
cam.set(4, 1964) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

oldname = ""

while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        if id == 12345:
            id = 1
        elif id == 12346:
            id = 2

        # Check if confidence is less then 100 ==> "0" is perfect match 
        if (confidence < 80):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "None"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1) 
         
        if oldname != (id):
            print(oldname)
            oldname = (id) 
            command = oldname.encode('utf-8')  
            
            s.send(command)
                      
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()




