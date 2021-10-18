import cv2
import numpy as np

def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhote = np.array([80,0,0])
    upperWhite = np.array([255,160,255])
    maskWhite = cv2.inRange(imgHsv, lowerWhote, upperWhite)
    return maskWhite

def warpImg(img, points, w, h):
    pts1 = np.float32(points)
    pts2=np.float([[0,0], [w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img, matrix, (w,h))
    return imgWarp

def nothing(a):
    pass

def initializeTrackbars(initialTrackbarVals, wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", initialTrackbarVals[0], wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", initialTrackbarVals[1], hT // 2, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", initialTrackbarVals[0], wT // 2, nothing)
    cv2.createTrackbar("Width Top", "Trackbars", initialTrackbarVals[0], wT // 2, nothing)


