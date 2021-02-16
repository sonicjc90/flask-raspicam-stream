# flask-raspicam-stream
A Flask web live stream server built for the Raspberry Pi Camera module. One client supported. 
It was insprired by [Miguel Grinbergs Streaming Video with Flask tutorial](https://blog.miguelgrinberg.com/post/video-streaming-with-flask). 

RPiCamera class serves the video stream as a separate class.
OpenCV is used to encode camera stream into jpeg images.

### Install Libraries
Add the following dependencies:

```bash
sudo apt-get update 
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python
```

### Usage
clone with : 
```bash

$ git clone https://github.com/CodeNextPaco/flask-raspicam-stream.git

```

Run the app, in the directory of app.py 
```bash

$ python3 app.py

```
On the pi,open a browser window to: **localhost:5000** . 5000 is the default debug port for Flask. On another client browser connected to the same wifi network, use the Pis IP address instead of localhost.

Only one client can access the livefeed. 
