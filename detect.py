import cv2
import os

video=cv2.VideoCapture(0)# Open Web_Cam

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


nameID=str(input("Enter Your NIC: ")).lower()

path='images/'+nameID

isExist = os.path.exists(path)

if isExist:
	print("You are Already registered")
	nameID=str(input("Enter Your NIC Again: "))
else:
	os.makedirs(path)

	#Detect face from the camera

while True:
	ret,frame=video.read()
	faces=facedetect.detectMultiScale(frame,1.3, 5)
	for x,y,w,h in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
	cv2.imshow("WindowFrame", frame)
    
	A=cv2.waitKey(1)
	if A==ord ('q'):
		break
video.release()
cv2.destroyAllWindows()
