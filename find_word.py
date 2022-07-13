import cv2
import math
import numpy as np
from operator import itemgetter

img = cv2.imread("E:/a_computer_design/test_picture/hsv_5.jpg")#读取存储路径
img = cv2.resize(img, (0, 0), fx=1, fy=1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

kernal = np.ones((3,3), np.uint8)

lower = np.array([0, 0, 0])
upper = np.array([255, 255, 69])

mask = cv2.inRange(hsv, lower, upper)
dilate = cv2.dilate(mask, kernal, iterations=2)

#imgand = cv2.bitwise_and(img, img, mask=mask)

contours, hierarchy = cv2.findContours(dilate, mode=cv2.RETR_EXTERNAL,
                                       method=cv2.CHAIN_APPROX_NONE)

xlist = []
ylist = []

for cn in contours:
    M = cv2.moments(cn)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])  # 计算质心
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 7, (255, 0, 255), -1)
        #cv2.putText(img, "word", (cX - 20, cY - 20),
        #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        print(cX, cY)
        xlist.append(cX)
        ylist.append(cY)

xlistsorted = []
xlistsorted = xlist[:]
xlist.sort()

z = []
for i in range(len(xlist)):
    z.append((xlist[i],ylist[i]))

z = sorted(z)




def get_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance


distlist = []

for i in range(len(xlist)):
   # print(i)
    if (i+1) != len(xlist):
        distlist.append(  get_distance(xlist[i], ylist[i], xlist[i+1], ylist[i+1]) )

prepareline = []
for i in range(len(xlist)):
    if (i+1) != len(xlist):
        prepareline.append((xlist[i],ylist[i], distlist[i]))


prepareline = sorted(prepareline, key = itemgetter(2))

line = []
for i in range(len(prepareline)):
    line.append((xlist[i], ylist[i],(prepareline[i][2]-prepareline[i+1][2])))
    prepareline.append((xlist[i],ylist[i], distlist[i]))

cv2.line(img, (z[7][0], z[7][1]), (z[9][0], z[9][1]), (0, 255, 0), 2)

print(distlist)
cv2.imshow('img', img)
cv2.imshow('imghsv', hsv)
cv2.imshow('mask', mask)
cv2.imshow('dilate', dilate)
# print(xlist)
print(z)
# print(prepareline)
# print(line)
cv2.waitKey(0)