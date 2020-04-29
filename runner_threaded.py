from threading import Thread
import cv2
from mtcnn import MTCNN

class VideoStreamWidget(object):
    def __init__(self, src=0):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)
        self.detector = MTCNN()

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Display frames in main program
        if self.status:

            result = self.detector.detect_faces(self.frame)
            for i in range(len(result)):
                bounding_box = result[i]['box']

                cv2.rectangle(self.frame,
                    (bounding_box[0], bounding_box[1]),
                    (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                    (0,155,255),
                    2)
            cv2.imshow('IP Camera Video Streaming', self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)


if __name__ == '__main__':
   
    video_stream_widget = VideoStreamWidget()
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass