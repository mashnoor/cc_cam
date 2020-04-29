
import cv2
import random
import string

from faced import FaceDetector
from faced.utils import annotate_image

vid_capture = cv2.VideoCapture('videos/office.mp4')
scale_percent = 100

face_detector = FaceDetector()
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def resize_image(image):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dsize = (width, height)

# resize image
    return cv2.resize(image, dsize)




while(True):
    detect = False
    # Capture each frame of webcam video
    ret,image = vid_capture.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #calculate the 50 percent of original dimensions
    image = resize_image(image)
    print(image.shape)

    bboxes = face_detector.predict(image, 0.9)
    ann_img = annotate_image(image, bboxes)
    #cv2.imshow('image', ann_img)
    out.write(ann_img)
    print(bboxes)

    
    #cv2.imshow("Camera", ann_img)
    if cv2.waitKey(1) &0XFF == ord('x'):
        vid_capture.release()
        out.release()
        break

vid_capture.release()
out.release()
cv2.destroyAllWindows()