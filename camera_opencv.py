import os
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
       # backSub = cv2.createBackgroundSubtractorKNN()
       # greenL = (0,25,25)
       # greenU = (100,255,255)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        while True:
            _, frame = camera.read()
           #blurred = cv2.GaussianBlur(frame, (11,11), 0)
           #hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
           #mask = cv2.inRange(hsv, greenL, greenU)

           #mask = cv2.rectangle(mask,(220,320),(300,460),(255,255,255),-1)

           #gray  = backSub.apply(frame)
           #mask = cv2.bitwise_not(mask)
           #color_mask = cv2.bitwise_and(gray,mask)
           #blur = cv2.GaussianBlur(color_mask, (5,5), 0)
           #_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
           #dilated = cv2.dilate(thresh, None, iterations=3)


           #contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
           #
           #
           #for contour in contours:
           #    (x,y,w,h)= cv2.boundingRect(contour)
           #    if cv2.contourArea(contour) < 700:
           #        continue
           #    if x<600 and y<100:
           #        continue
           #    cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
           #cv2.putText(frame, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 3)
          # cv2.drawContours(frame, contours, -1, (0,255,0),2)

           # encode as a jpeg image and return it
            yield cv2.imencode('.jpg',frame)[1].tobytes()
