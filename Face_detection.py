import cv2

# Creating the CascadeClassifier Object
face_cascade = cv2.CascadeClassifier('C:\\Users\\PycharmProjects\\opencv\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

#Reading the image as it is
img = cv2.imread("E:\\CV\\Johnny-Depp.jpg")

#Reading the image as gray scale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Search the cordinates of the image
face = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,
                                     minNeighbors=5)

print(type(face))
print(face)

for x,y,w,h in face:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255),3)


cv2.imshow("Gray",img)

cv2.waitKey(0)

cv2.destroyAllWindows()


