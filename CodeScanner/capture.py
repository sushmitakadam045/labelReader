"""
This Python script captures an image using camera.

It performs the following tasks:
1. Connect to the first camera
2. Capture an image

Usage:
    python capture.py

Dependencies:
    opencv2
"""

import CodeScanner.cameraSettings as cameraSettings
import cv2


def applySettings(cap):
    camSet = cameraSettings.CameraSettingsCls()
    camSet.load_config()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camSet.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camSet.height)
    cap.set(cv2.CAP_PROP_CONTRAST, camSet.contrast)
    cap.set(cv2.CAP_PROP_SATURATION, camSet.saturation)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, camSet.brightness)
    cap.set(cv2.CAP_PROP_GAIN, camSet.gain)
    cap.set(cv2.CAP_PROP_EXPOSURE, camSet.exposure)
    cap.set(cv2.CAP_PROP_FPS, camSet.fps)


def captureImage():
    cap = cv2.VideoCapture(0)
    #applySettings(cap)

    if not cap.isOpened():
        raise IOError("Could not open camera!")

    ret, frame = cap.read()

    if not ret:
        raise IOError("Could not read frame.")

    cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return  frame
