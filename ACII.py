import cv2
import numpy as np

# Define the ASCII characters to use
ASCII_CHARS = ["-", "@", "|", "%", "?", "*", "+", ";", ":", ",", "."]

class VideoToAscii:
    def __init__(self, device_id=0, width=180, height=60, scale_factor=0.05):
        self.cap = cv2.VideoCapture(device_id)
        self.width = width
        self.height = height
        self.scale_factor = scale_factor
    
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
    
    def _pixel_to_ascii(self, pixel):
        """
        Converts an RGB pixel to an ASCII character.

        @param pixel: The input pixel as an array of RGB values.
        @return: The corresponding ASCII character.
        """
        r, g, b = pixel
        brightness = int((r + g + b) / 3)
        ascii_char = ASCII_CHARS[int(brightness / 255 * (len(ASCII_CHARS) - 1))]
        return ascii_char
    
    def process_video(self):
        while True:
            # Capture a frame from the video capture device
            ret, frame = self.cap.read()

            # Resize the frame to the desired dimensions
            frame = cv2.resize(frame, (self.width, self.height))

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Compute the ASCII representation of the frame
            ascii_str = ""
            for row in gray:
                for pixel in row:
                    ascii_str += self._pixel_to_ascii([pixel, pixel, pixel])
                ascii_str += "\n"
            
            # Display the ASCII representation of the frame
            print("\n"*10, ascii_str)

            # Wait for a key press to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    app = VideoToAscii()
    app.process_video()