import cv2
import numpy as np

START = (0,0)
END = (512,512)
COLOR = (255,0,0)
THICKNESS = 5

 
image = np.zeros([512,512,3] , dtype=np.uint8)
print(image.shape)

img = cv2.line(image , START , END , COLOR ,THICKNESS)
cv2.imshow("image" , img)
cv2.waitKey(0)

image1 = cv2.arrowedLine(image , (0,0) , (255,255) , (255,0,0) , 5)

cv2.imshow("image" , image1)

cv2.waitKey(0)


img2 = cv2.rectangle(image , (100,100) , (255,255) , (0,255,0) , 5)
cv2.imshow("image" , img2)
cv2.waitKey(0)

img3 = cv2.circle(image,(255,255) , (100) , (0,0,255) , 10)
cv2.imshow("image" , img3)
cv2.waitKey(0)

img4 = cv2.putText(image,"Image Geometry",(0,400) , cv2.FONT_HERSHEY_COMPLEX,1.5,(55,100,255) ,4)
cv2.imshow("image" , img4)
cv2.waitKey(0)


cv2.destroyAllWindows()