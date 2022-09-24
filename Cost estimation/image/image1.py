import cv2 as cv
img1=cv.imread('C:\\Users\DELL\Downloads\\plan.jpg')
# img2=cv.imread('C:\\Users\DELL\Downloads\\indian-style-1000-square-feet-house-plan-design.jpg')
cv.imshow('image',img1)
# cv.imshow('image',img2)
# cv.waitKey(0)
cv.waitKey(0)

# def rescaleFrame(frame,scale=0.75):
#     width=int(frame.shape[1]*scale)
#     height = int(frame.shape[0] * scale)
#
#     dimensions=(width,height)
#
#     return  cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)