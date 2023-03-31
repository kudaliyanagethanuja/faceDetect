import cv2
import os
#import detect
#import webcam

video=cv2.VideoCapture(0)#Open Web_cam

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


count=0

#cap=cv2.VideoCapture(0)
#cap.set(3, 640)
#cap.set(4, 480)
#font=cv2.FONT_HERSHEY_COMPLEX

nameID=str(input("Enter Your NIC: ")).lower()

path='images/'+nameID

isExist = os.path.exists(path)

if isExist:
	print("You are Already registered")
	nameID=str(input("Enter Your NIC Again: "))
else:
	os.makedirs(path)

while True: #Dectect face
    
	ret,frame=video.read()
	
	faces=facedetect.detectMultiScale(frame,1.3, 5)
	
	for x,y,w,h in faces:
            
		count=count+1 #Collect user's faces
		name='./images/'+nameID+'/'+ str(count) + '.jpg'
		print("Creating Images........." +name)
		
		cv2.imwrite(name, frame[y:y+h,x:x+w])
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
		
	cv2.imshow("WindowFrame", frame)
	cv2.waitKey(1)
	if count>50:
		break
	    
video.release()
cv2.destroyAllWindows()
