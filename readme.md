# Face Detection App

This is a Python application for real-time face detection using OpenCV.

## Installation

1. Clone this repository to your local machine.
2. Install the necessary packages using pip: `pip install -r requirements.txt`

## Usage

To run the application, simply execute `python facedetectorapp.py` from the command line. The app will use your webcam to capture live video and detect faces in real-time.

Press `ESC` to exit the application.

## Configuration

The application can be configured by editing the `config.ini` file. The following options are available:

### Video

- `width`: the width of the video capture (default: 640)
- `height`: the height of the video capture (default: 480)

### Font

- `face`: the font face to use (default: `cv2.FONT_HERSHEY_SIMPLEX`)
- `size`: the font size (default: 0.7)
- `thickness`: the font thickness (default: 2)
- `color`: the font color in BGR format (default: 255, 255, 255)

### Status

- `text`: the status text to display (default: "Running")
- `color`: the status text color in BGR format (default: 0, 255, 0)
