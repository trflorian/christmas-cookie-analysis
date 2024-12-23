import cv2

img = cv2.imread("images/cookies.jpg")

cv2.imshow("Cookies", img)
cv2.waitKey(0)

cv2.destroyAllWindows()