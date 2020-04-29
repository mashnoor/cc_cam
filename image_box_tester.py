
import cv2
from mtcnn import MTCNN
from face_recognition import FaceRecognition

detector = MTCNN()
fr = FaceRecognition()


image = cv2.cvtColor(cv2.imread("test.png"), cv2.COLOR_BGR2RGB)

print(fr.predict(image))
exit()

result = detector.detect_faces(image)

# Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
bounding_box = result[0]['box']
keypoints = result[0]['keypoints']

cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              2)

bounding_box = result[1]['box']
cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              2)

bounding_box = result[2]['box']
cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              2)

cv2.imwrite("test_drawn.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

print(result)