from flask import Flask, render_template, Response
from rpi_camera import RPiCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


#the generator, a special type of function that yields, instead of returns.
def gen(camera):

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