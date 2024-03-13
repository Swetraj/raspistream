
## Simple Real-time Video Streaming Server

**Description**

This Python project establishes a basic video streaming server using OpenCV, socket programming, and pickle for data serialization. The server captures video frames from a webcam, compresses them, and transmits the compressed image data over UDP to a connected client.

**Dependencies**

* Python 3+
* OpenCV (cv2)
* Socket
* Pickle

**Installation**

1. Make sure you have Python 3 installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install the required libraries:

   ```bash
   pip install opencv-python socket pickle
   ```

**Usage**

1. **Start the server:**

   ```bash
   python server.py
   ```

   This will start the server, and it will print the server's IP address and port.

2. **Connect a client:**

   To receive the video stream, you'll need a client that can receive and decode the UDP packets. (**Note:** A sample client is not provided in this code)

