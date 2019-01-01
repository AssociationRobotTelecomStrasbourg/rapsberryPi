# Aruco
Aruco is an opencv library allows to create and to detect markers like "QRCode". It's very useful in a case of robot pose estimation.

## Prerequisites

We need to install OpenCV.

## OpenCV

See : [Our OpenCV wiki](https://github.com/AssociationRobotTelecomStrasbourg/raspberryPi/wiki/OpenCV)

## Tests
You can try to detect aruco marker with the image `../imageRasp/aruco/2Markers2-5_2.jpg`


## Python codes

### arucoCreation
Save a marker in `../imageRasp/aruco/`

```
python arucoCreation.py  <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Size of image (px)> <Id of marker>
```

### arucoDetection
Detection of marker in a real marker (direct result of drawMarker function or arucoCreation script)

```
python arucoDetection.py <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Path of marker image>
```

### photoDetection
Detection of marker in real image.

```
python photoDetection.py <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Path of marker image>
```

### videoDetection
Detection of marker with a PiCamera. (Modify the file to have want you expect)

```
python videoDetection.py
```

### charucoBoard
Create a charucoBoard in `../imageRasp/aruco/`

```
python charucoBoard.py <squaresX> <squaresY> <squareLength> <markerLength> <sizeXImg> <sizeYImg>
```


### cameraCalibration

The file `calibration.py` takes images in `./imageRasp/aruco/charucoBoard/` to calibrate the camera.

To calibrate your camera you need to take photo of a printed charucoBoard and feed them to `calibration.py` line 12.

## Authors
* **Sorgan** - Aruco project

## See also
[OpenCV Aruco detection](https://docs.opencv.org/3.4.3/d5/dae/tutorial_aruco_detection.html)

[OpenCV Calibration with Aruco](https://docs.opencv.org/3.4.3/da/d13/tutorial_aruco_calibration.html)

[Calibration with ArUco and ChArUco](https://docs.opencv.org/3.4.5/d9/d0c/group__calib3d.html#ga3207604e4b1a1758aa66acb6ed5aa65d)
