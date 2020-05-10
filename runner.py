import cv2
from my_face_recognition.face_recognition import FaceRecognition

vid_capture = cv2.VideoCapture('videos/office.mp4')
scale_percent = 60
fr = FaceRecognition()
fr.load("model.pkl")

def resize_image(image):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dsize = (width, height)

    # resize image
    return cv2.resize(image, dsize)




while (True):
    ret, image = vid_capture.read()

    image = resize_image(image)

    cv2.imshow("Camera", fr.predict(image))
    if cv2.waitKey(1) & 0XFF == ord('x'):
        break
