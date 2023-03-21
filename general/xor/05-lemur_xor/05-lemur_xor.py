import cv2

img1 = cv2.imread('lemur.png')
img2 = cv2.imread('flag.png')

xor_img = cv2.bitwise_xor(img1, img2)

cv2.imshow('Flag', xor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()