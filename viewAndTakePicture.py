import time
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

# Start the camera and define settings
camera = PiCamera()
camera.resolution = (600, 400) # A smaller resolution means faster processing
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(600, 400))

# Give camera time to warm up
time.sleep(0.1)

nbPic=0
# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Take the frame as an array, convert it to black and white, and look for facial features
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the resulting image
    cv2.imshow("Display", image)

    # Clear the stream capture
    rawCapture.truncate(0)

    #set "q" as the key to exit the program when pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c") :
        nbPic = nbPic + 1;
        camera.capture('/home/pi/Desktop/image%s.jpg' % nbPic)
