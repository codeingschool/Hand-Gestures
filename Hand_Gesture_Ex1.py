import cv2
import numpy as np

hand = cv2.imread('Capture.png',0)

ret, the = cv2.threshold(hand, 70, 255, cv2.THRESH_BINARY)

_,contours,_ = cv2.findContours(the.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(c) for c in contours]
final = cv2.drawContours(hand, hull, -1, (255,0,0))

cv2.imshow('Originals', hand)
cv2.imshow('Thresh',the)
cv2.imshow('Convex hull',final)

cv2.waitKey(0)
cv2.destroyAllWindows()