import cv2 
import matplotlib.pyplot as plt
 
image = cv2.imread(r'children.jpg')

face_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_path)

grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

for(x,y,w,h) in faces :
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Canny change Children',image)
cv2.waitKey(0)
cv2.destroyAllWindows()