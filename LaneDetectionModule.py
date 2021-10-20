import cv2
import numpy as np
import utlis

def getLaneCurve(img):
    imgCopy = img.copy()

    ####STEP 1
    imgThres=utlis.thresholding(img)

    ####STEP 2
    h,w,c =  img.shape

    points = utlis.valTrackBars()
    imgWarp=utlis.warpImg(img, points, w,h)
    imgWarpPoints = utlis.drawPoints(img, points)

    imgThres = cv2.resize(imgThres, (480, 240))
    imgWarp = cv2.resize(imgWarp, (480, 240))
    imgWarpPoints = cv2.resize(imgWarpPoints, (480, 240))

    #### STEP 3
    basePoint, imgHist =  utlis.getHistogram(imgWarp, display=True)

    cv2.imshow("Thres", imgThres)
    cv2.imshow("Warp", imgWarp)
    cv2.imshow("Warp Points", imgWarpPoints)
    cv2.imshow("Histogram", imgHist)
    return None

if __name__=='__main__':
    cap =cv2.VideoCapture('vid1.mp4')
    initialTrackBarsVals = [96,667,162,100]
    utlis.initializeTrackbars(initialTrackBarsVals)
    frameCounter = 0
    while True:
        frameCounter+=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set((cv2.CAP_PROP_POS_FRAMES), 0)
            frameCounter = 0


        success, img=cap.read()
        getLaneCurve(img)

        img = cv2.resize(img, (480,240))
        cv2.imshow('Vid', img)
        cv2.waitKey(1)