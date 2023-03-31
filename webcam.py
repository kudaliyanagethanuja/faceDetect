import cv2
import os

##Open web_Cam

video=cv2.VideoCapture(0)

nameID=str(input("Enter Your NIC: ")).lower()

path='images/'+nameID

isExist = os.path.exists(path)

if isExist:
	print("You are Already Ragistered")
	nameID=str(input("Enter Your NIC Again: "))
else:
	os.makedirs(path)



while True:
	ret,frame=video.read()
	cv2.imshow("WindowFrame", frame)
	A=cv2.waitKey(1)
	if A==ord ('q'):
		break
video.release()
cv2.destroyAllWindows()
