import cv2
import numpy as np


img = cv2.imread("E:/a_computer_design/test_picture/better_pic.jpg")#读取存储路径
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#cv2.circle(img, (120, 260), 7, (255, 0, 255), -1)

cv2.imshow("img", img)
# #########################################################################
# points1 = np.float32([[120, 290], [900, 0], [100, 650], [900, 690]])
# points2 = np.float32([[0,0], [900,0], [0,690], [900,690]])
#
# #计算得到转换矩阵
# M = cv2.getPerspectiveTransform(points1, points2)
#
# # 实现透视变换转换
# processed = cv2.warpPerspective(img, M, (900,690))

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",550,560)
#调节单元名称，调节窗口名称，初始值，最大值
cv2.createTrackbar("Hue Min","TrackBars",0,255,empty)
cv2.createTrackbar("Hue Max","TrackBars",255,255,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# mask_name_ppt = ['mask1:', 'mask2:', 'mask3:', 'mask4:', 'mask5:', 'mask6:']
# mask_value_ppt = [(27,168,211,39,242,253), (0,26,153,99,71,215),(65,32,203,95,87,249),(135,76,29,227,148,62),
#                   (63,141,137,95,189,156),(197,105,69,226,138,93)]
# for i in range(len(mask_name_ppt)):
#     print(mask_name_ppt[i])
#     print(mask_value_ppt[i])



while True:
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(hsv, lower, upper)
    #result = cv2.bitwise_and(img, img, mask=mask)
  #  cv2.imshow('img_pro', processed)
    cv2.imshow('mask', mask)
    #cv2.imshow('result', result)
    cv2.waitKey(1)


