from flask import Flask, render_template, Response
from rpi_camera import RPiCamera
import picamera
import datetime
import time
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


#the generator, a special type of function that yields, instead of returns.
def gen(camera):

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(10)
    camera.stop_recording()

    while True:
        frame = camera.get_frame()

        # Each frame is set as a jpg content type. Frame data is in bytes.
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/stream')
def stream():

    feed = Response(gen(RPiCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

    print(type(feed))
    return feed

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True )