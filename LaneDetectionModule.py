import cv2
import numpy as np
import utlis

def getLaneCurve(img):

    ####STEP 1
    imgThres=utlis.thresholding(img)

    ####STEP 2
    h,w,c =  img.shape

    #imgWarp=utlis.warpImg(img, points, w,h)


    cv2.imshow("Thres", imgThres)
    return None

if __name__=='__main__':
    cap =cv2.VideoCapture('video')
    while True:
        success, img=cap.read()
        getLaneCurve(img)

        img = cv2.resize(img, (480,240))
        cv2.imshow('Vid', img)
        cv2.waitKey(1)