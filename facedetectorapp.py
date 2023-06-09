import cv2
import time
from facedetector import FaceDetector
from videocapture import VideoCapture
import configparser
import threading

class FaceDetectorApp:
    def __init__(self, config_file):
        """
        Constructor for the FaceDetectorApp class.
        Initializes the FaceDetector and VideoCapture objects, and the font for displaying text.
        """
        config = configparser.ConfigParser()
        config.read(config_file)
        self.width = int(config.get('VIDEO', 'width'))
        self.height = int(config.get('VIDEO', 'height'))
        self.face_detector = FaceDetector()
        self.video_capture = VideoCapture()
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = float(config.get('FONT', 'size'))
        self.font_thickness = int(config.get('FONT', 'thickness'))
        self.font_color = tuple(map(int, config.get('FONT', 'color').split(',')))
        self.status_text = config.get('STATUS', 'text')
        self.status_color = tuple(map(int, config.get('STATUS', 'color').split(',')))
        self.is_running = False
        self.debug = config.getboolean('DEBUG', 'DEBUG')
        if self.debug:
            print('[program] starting...')

    def _run(self):
        """
        Internal method for running the face detector application in a separate thread.
        """
        if self.debug:
            print('[program] start')
        while self.is_running:
            ret, frame = self.video_capture.read()
            if not ret:
                break
            faces = self.face_detector.detect_faces(frame)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h),self.status_color, 2)
                cv2.putText(frame, f"X: {x}, Y: {y}", (x, y - 10), self.font, self.font_size, self.status_color, self.font_thickness, cv2.LINE_AA)
            elapsed_time = time.time() - self.video_capture.start_time
            if elapsed_time > 0:
                fps = self.video_capture.num_frames / elapsed_time
            else:
                fps = 0
            fps_text = 'FPS: {:.2f}'.format(fps)
            resolution_text = 'Resolution: {}x{}'.format(frame.shape[1], frame.shape[0])
            cv2.putText(frame, fps_text, (10, 30), self.font, self.font_size, self.font_color, self.font_thickness, cv2.LINE_AA)
            cv2.putText(frame, resolution_text, (10, 60), self.font, self.font_size, self.font_color, self.font_thickness, cv2.LINE_AA)
            cv2.putText(frame,f"Status: {self.status_text}", (10, 90), self.font, self.font_size, self.status_color, self.font_thickness, cv2.LINE_AA)
            cv2.imshow('Face Detector', frame)
            key = cv2.waitKey(1)
            if key == 27: # press ESC to exit
                break

        if self.debug:
            print('[program] stop')

    def run(self):
        """
        Runs the face detector application in a separate thread.
        """
        self.is_running = True
        thread = threading.Thread(target=self._run)
        thread.start()

    def stop(self):
        """
        Stops the face detector application.
        """
        self.is_running = False
        self.video_capture.release()
        cv2.destroyAllWindows()
        if self.debug:
            print('[program] exit')



if __name__ == '__main__':
    app = FaceDetectorApp('config.ini')
    app.run()
