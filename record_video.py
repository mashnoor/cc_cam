import cv2

#Capture video from webcam
vid_capture = cv2.VideoCapture(0)
size = (int(vid_capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(vid_capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.cv.FOURCC('8', 'B', 'P', 'S')     #works, large
out = cv2.VideoWriter("output.avi", fourcc, 20.0, size, True)
while(True):
     # Capture each frame of webcam video
     ret,frame = vid_capture.read()
     cv2.imshow("My cam video", frame)
     frame = cv2.flip(frame,0)
     out.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break

# close the already opened camera
vid_capture.release()
# close the already opened file
out.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()