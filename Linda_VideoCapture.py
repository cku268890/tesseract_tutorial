import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# (2304, 1536)
file_name = 'L2_{}.mp4 '.format(datetime.now().strftime('%Y%m%d%H%M%S'))
# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('L2_20210907_1.avi',fourcc, 20.0, (960,720))
out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'mp4v'), 3, (1920,1080))
video_start = False
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1024, 768))
    #print(frame.shape)
    if ret==True:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        
        
        cv2.imshow('frame',frame)
        if video_start:
            out.write(frame)
        key = cv2.waitKey(1)

        if key == ord('s'):
            video_start = True
        elif key == ord('x'):
            now = datetime.now().strftime('%Y%m%d%H%M%S')
            cv2.imwrite(now + ".png", frame)
        elif key == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows() 
