import time
import cv2

#if using the picamera, import those libraries as well
from picamera.array import PiRGBArray
from picamera import PiCamera

#start the camera and define settings
camera = PiCamera()
camera.resolution = (320, 240) #a smaller resolution means faster processing
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
