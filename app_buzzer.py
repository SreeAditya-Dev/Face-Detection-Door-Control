import cv2 # type: ignore
from cvzone.FaceDetectionModule import FaceDetector # type: ignore
import serial # type: ignore
import time

detector = FaceDetector()
video = cv2.VideoCapture(0)
arduino = serial.Serial('COM10', 9600) # if you use left USB port COM9 or if you use right side USB port COM10
time.sleep(2)

while True:
    ret, frame = video.read()
    img, bboxs = detector.findFaces(frame)

    if bboxs:
        print("Face detected")
        arduino.write(b'1')
    else:
        print("No face detected")
        arduino.write(b'2')

    cv2.imshow("Face Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
arduino.close()