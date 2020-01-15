# image capturing in python

# importing opencv 
import cv2
import time

#now i can load any image by using camera
cap=cv2.VideoCapture(0)

# now taking pic
status,frame =  cap.read()

print(frame.shape)

cv2.imshow('windoname1',frame)

cv2.waitKey(0) # 0 mean unlimited time

'''
imgnew=img[0:200,200:500]


# to show image
cv2.imshow('windowname',imgnew)
# to show img
cv2.imshow('windowname1',img)
cv2.imshow('windowname2',img1)

'''