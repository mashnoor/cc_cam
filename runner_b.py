import cv2
from mtcnn import MTCNN
import random
import string
import pandas as pd

detector = MTCNN()

vid_capture = cv2.VideoCapture('videos/office.mp4')
scale_percent = 30


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def resize_image(image):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dsize = (width, height)

    # resize image
    return cv2.resize(image, dsize)


while (True):
    detect = False
    # Capture each frame of webcam video
    ret, image = vid_capture.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # calculate the 50 percent of original dimensions
    image = resize_image(image)
    # print(image.shape)
    show = False

    result = detector.detect_faces(image)
    for i in range(len(result)):
        detect = True
        bounding_box = result[i]['box']
        confidence = result[i]['confidence']

        if confidence >= 0.9:
            print(confidence)

            cv2.rectangle(image,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0, 155, 255),
                          2)
            cv2.putText(image, 'Fedex', (bounding_box[0], bounding_box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (36, 255, 12), 2)
    if detect == True:
        # cv2.imwrite(randomString() + ".jpg", image)
        detect = False
    cv2.imshow("Camera", image)
    if cv2.waitKey(1) & 0XFF == ord('x'):
        break
