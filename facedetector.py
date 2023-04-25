import cv2

class FaceDetector:
    def __init__(self):
        """
        Constructor for the FaceDetector class.
        Initializes the face cascade classifier.
        """
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
    def detect_faces(self, img):
        """
        Detects faces in the given image.

        @param img: The input image.
        @return: A list of tuples representing the coordinates of the faces.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
