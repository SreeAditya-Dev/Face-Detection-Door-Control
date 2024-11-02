import cv2  # type: ignore
from cvzone.FaceDetectionModule import FaceDetector  # type: ignore
import serial  # type: ignore
import time
import pyttsx3  # Import the pyttsx3 library for TTS

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

detector = FaceDetector()
video = cv2.VideoCapture(0)
arduino = serial.Serial('COM9', 9600)  # if you use left USB port COM9 or if you use right side USB port COM10 for your setup
time.sleep(2)  # Give the Arduino time to initialize

while True:
    ret, frame = video.read()
    img, bboxs = detector.findFaces(frame)

    if bboxs:
        print("Face detected")
        arduino.write(b'1')  # Send '1' to rotate the servo motor
        tts_engine.say("Door open")  # Speak "Door open"
        tts_engine.runAndWait()
    else:
        print("No face detected")
        arduino.write(b'2')  # Send '2' to turn on the LED
        tts_engine.say("Door close")  # Speak "Door close"
        tts_engine.runAndWait()

    cv2.imshow("Face Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
arduino.close()
