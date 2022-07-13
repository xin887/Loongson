import cv2
import math
import numpy as np
from operator import itemgetter

img = cv2.imread("E:/a_computer_design/test_picture/market_door/market_door_1.jpg")#读取存储路径
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

kernal_d = np.ones((3,3), np.uint8)
kernal_e = np.ones((3,3), np.uint8)

lower = np.array([101, 99, 127])
upper = np.array([120, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
imgblur1 = cv2.GaussianBlur(mask,(3,3),10,10)
cv2.imshow('img_blur', imgblur1)
#img_erosion = cv2.erode(imgblur1, kernal_e, iterations=1)
#cv2.imshow('img_er', img_erosion)
dilate = cv2.dilate(imgblur1, kernal_d, iterations=2)
cv2.imshow('img_di', dilate)

#imgand = cv2.bitwise_and(img, img, mask=mask)

contours, hierarchy = cv2.findContours(dilate, mode=cv2.RETR_EXTERNAL,
                                       method=cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(dilate,contours,-1,(0,255,255),10)

xlist = []
ylist = []
area = 0

for cn in contours:
    M = cv2.moments(cn)
    area += cv2.contourArea(cn)
    print('area = ')
    print(area)
    if area > 2000:
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])  # 计算质心
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 7, (255, 0, 255), -1)
            #cv2.putText(img, "word", (cX - 20, cY - 20),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            print(cX, cY)
            xlist.append(cX)
            ylist.append(cY)
        # area += cv2.contourArea(cn)
        # print('area = ')
        # print(area)



# cv2.circle(img, (100, 300), 7, (0, 0, 255), -1)


z = []
for i in range(len(xlist)):
    z.append((xlist[i],ylist[i]))

z = sorted(z)

#cv2.line(img, (z[7][0], z[7][1]), (z[9][0], z[9][1]), (0, 255, 0), 2)


cv2.imshow('img', img)
#cv2.imshow('imghsv', hsv)
cv2.imshow('mask', mask)
cv2.imshow('dilate', dilate)
# print(xlist)
print(z)
# print(prepareline)
# print(line)
cv2.waitKey(0)