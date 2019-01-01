import time
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

# Start the camera and define settings
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 32
rawCapture = PiRGBArray(camera)

# Give camera time to warm up
time.sleep(0.1)

nbPic=0
# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Take the frame as an array, convert it to black and white
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
        camera.capture('/home/pi/raspberryPi/imageRasp/image%s.jpg' % nbPic)
        print("Pictuuuure !")
    # "v" to capture photo
    if key == ord("v") :
        camera.start_recording('/home/pi/raspberryPi/imageRasp/video.h264')
        print("Start video")
    # "v" to capture photo
    if key == ord("b") :
        camera.stop_recording()
        print("Stop video")
cv2.destroyAllWindows()
