import cv2
import cvzone

img = cv2.imread("test_images\\20240221_192151.jpg")
img = cv2.resize(img, (800,600))

def preProcessing(img):
    imgPre = cv2.GaussianBlur(img, (5,5), 4)
    return imgPre

imgPre = preProcessing(img)

cv2.imshow("Img", img)
cv2.imshow("ImgPre", imgPre)
cv2.waitKey(0)
cv2.destroyAllWindows()