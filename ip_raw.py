import cv2
import numpy as np

## Top left - 84,4
## Top right - 594,9
## Bottom left - 73,479
## Bottom right - 626,462

video = cv2.VideoCapture(0)
points_1 = np.float32([(84,4),(594,9),(73,479),(626,462)]) 
points_2 = np.float32([(0,0),(640,0),(0,480),(640,480)])

while True:
    _,frame = video.read()

    perspective_transform = cv2.getPerspectiveTransform(points_1,points_2)
    dst = cv2.warpPerspective(frame,perspective_transform,(640,480))

    cv2.imshow('frame',dst)
    k = cv2.waitKey(5) & 0xFF   #Waiting for the 'Esc' button to be pressed
    if k == 27:
        break

cv2.destroyAllWindows()    #close all the windows
video.release()
