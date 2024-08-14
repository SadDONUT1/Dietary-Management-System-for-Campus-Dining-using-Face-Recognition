import cv2 #OpenCV 

#classifier                            #paths of face initionlising algorthm file 
faceCascade = cv2.CascadeClassifier('/Users/wonseokhan/Desktop/Visual Studio Code/Python/EPQ/safemeal/haarcascade_frontalface_default.xml')

#video caputure setting
capture = cv2.VideoCapture(0) # initialize, # is camera number
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1280) #CAP_PROP_FRAME_WIDTH == 3
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,720) #CAP_PROP_FRAME_HEIGHT == 4

#console message
face_id = input('\n Enter student id and press enter ==> ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

count = 0 # # of caputre face images
while True: 
    ret, frame = capture.read() #camara & frames
    frame = cv2.flip(frame, 1) #fliping vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting colour into black & white: reduce storage
    
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2, #search window scale has to be bigger than 1
        minNeighbors = 6, #minimum distance between face in pixels
        minSize=(30, 30) #minimum face size, if smaller ignore
    )
    
    #printing rectangle around face, passing the x & y coordinates, take in the parameter of colour, thickness & line type
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        count += 1
        cv2.imwrite("/Users/wonseokhan/Desktop/Visual Studio Code/Python/EPQ/safemeal/dataset/"+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h, x:x+w])
        cv2.imshow('image',frame)

    #종료 조건
    if cv2.waitKey(1) > 0 : break #any key pressed will stop the program
    elif count >= 1000 : break #number of face sample

print("\n [INFO] Exiting Program")

capture.release() #release memery
cv2.destroyAllWindows()#close alll the window