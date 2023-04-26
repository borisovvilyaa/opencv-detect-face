import cv2
import time
import configparser
class FaceDetector:
    def __init__(self):
        """
        Constructor for the FaceDetector class.
        Initializes the face cascade classifier.

        @param debug: Whether to enable debug mode.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.debug = config.getboolean('DEBUG', 'DEBUG')
        
    def detect_faces(self, img):
        """
        Detects faces in the given image.

        @param img: The input image.
        @return: A list of tuples representing the coordinates of the faces.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        start_time = time.time()
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        end_time = time.time()

        # if self.debug:
        #     for (x, y, w, h) in faces:
        #         print(f"[DEBUG] Time taken to detect faces: {end_time - start_time:.2f}s")
        #         print(f"[DEBUG] Face detected at ({x}, {y}) with width={w} and height={h}")

        return faces
