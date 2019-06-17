import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
text = ""


color = (0,0,255) #BGR

cap = cv2.VideoCapture(0) #0 means first webcam

frames = []
counter = 0

threshold = 1

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts captured frame to Grayscale for easier analysis
    
    frames.append(gray)
    cv2.putText(frame,text,(5,30), font, 1, color, 3, cv2.LINE_AA) #may need to change some arguments 

    cv2.imshow('frame',frame)
    
    
    if counter > 0:
        difference = cv2.subtract(cv2.medianBlur(frames[counter],15),cv2.medianBlur(frames[counter-1],15)) #applies median blur before subtracting for noise reduction 
        #cv2.imshow('difference',difference)
        mean = np.mean(difference)
        #print(mean)
        if mean > threshold:
            text = "Motion Detected"
        else:
            text = ""
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #Press q to quit video capture
        break
    
    counter = counter + 1
    

cap.release()
cv2.destroyAllWindows()


