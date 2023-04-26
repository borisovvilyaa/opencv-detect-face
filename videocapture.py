import cv2
import time
import configparser


class VideoCapture:
    def __init__(self):
        """
        Constructor for the VideoCapture class.
        Initializes the video capture object and sets the resolution.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.getint('VIDEO', 'width'))
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.getint('VIDEO', 'height'))
        self.num_frames = 0
        self.start_time = time.time()
        self.frame_rate = 0
        self.debug = config.getboolean('DEBUG', 'DEBUG')
        if self.debug:
            print("[Webcamera] Video capture started.")

        
    def read(self):
        """
        Reads a frame from the video capture.

        @return: A tuple containing a boolean indicating whether the frame was successfully read, and the frame.
        """
        ret, frame = self.cap.read()
        self.num_frames += 1
        return ret, frame

    def release(self):
        """
        Releases the video capture.
        """
        self.cap.release()
