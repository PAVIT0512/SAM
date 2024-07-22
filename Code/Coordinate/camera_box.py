import camera
import cv2

cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    cv2.imshow("image",frame)
    print(camera.boxdetection(frame))
    break

cv2.destroyAllWindows()



# def capture_img():
#     img=cv2.VideoCapture(0)

#     result,image=img.read()
#     if result:
#         points=camera.boxdetection(image)
#         cv2.waitKey(3000)
#         return points
#     else:
#         print("No image detected. Please! try again")

# capture_img()