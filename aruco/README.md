# Aruco
Aruco is an opencv library allows to create and to detect markers. It's very useful in a case of robot pose estimation.

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
python raspDetection
```

## Authors
* **Alexis ROLLAND** - *Initial work*

## See also
[OpenCV Aruco detection](https://docs.opencv.org/3.1.0/d5/dae/tutorial_aruco_detection.html)
