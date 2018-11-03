# Aruco
Aruco is an opencv library allows to create and to detect markers like "QRCode". It's very useful in a case of robot pose estimation.

## Prerequisites

We need to install OpenCV.

## OpenCV

See : [Our OpenCV wiki](https://github.com/AssociationRobotTelecomStrasbourg/raspberryPi/wiki/OpenCV)

## Python codes

### arucoCreation
Save a marker in `raspberryPi/imageRasp/aruco/`

```
python arucoCreation.py  <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Size of image (px)> <Id of marker>
```

### arucoDetection
Detection of marker in a real marker (direct result of drawMarker function or arucoCreation script)

```
python arucoDetection.py <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Path of marker image>
```

### detection
Detection of marker in real image.

```
python detection.py <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Path of marker image>
```

### raspDetection
Detection of marker with a PiCamera.
```
python raspDetection.py
```

## Authors
* **Alexis ROLLAND**

## See also
[OpenCV Aruco detection](https://docs.opencv.org/3.4.3/d5/dae/tutorial_aruco_detection.html)
[OpenCV Calibration with Aruco](https://docs.opencv.org/3.4.3/da/d13/tutorial_aruco_calibration.html)
