import cv2
import numpy as np

def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhote = np.array([75,0,0])
    upperWhite = np.array([255,160,255])
    maskWhite = cv2.inRange(imgHsv, lowerWhote, upperWhite)
    return maskWhite

def warpImg(img, points, w, h):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0], [w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img, matrix, (w,h))
    return imgWarp

def nothing(a):
    pass

def initializeTrackbars(initialTrackbarVals, wT=1080, hT=720):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", initialTrackbarVals[0], wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", initialTrackbarVals[1], hT , nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", initialTrackbarVals[2], wT // 2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", initialTrackbarVals[3], hT, nothing)

def valTrackBars(wT=1080, hT=720):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop , heightTop), (widthBottom, heightBottom), (wT-widthBottom, heightBottom)])
    return  points

def drawPoints(img, points):
    for x in range(4):
        cv2.circle(img, (int(points[x][0]), int (points[x][1])), 15, (0,0,255), cv2.FILLED)
    return img

def getHistogram(img, minPier=0.1, display=False):
    histValues = np.sum(img, axis=0)
    #print(histValues)
    maxValue = np.max(histValues)
    minValue = np.min(histValues)

    indexArray = np.where(histValues>=minValue)
    basePoint = int(np.average(indexArray))
    print(basePoint)

    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            print((x,img.shape[0]))
            print(x, intensity[0]/255)
            cv2.line(imgHist, (x,img.shape[0]), (x, img.shape[0] - int(intensity[0]/255)), (255,0,255), 1)
            cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0,255,255), cv2.FILLED)
        return basePoint, imgHist
    return basePoint
