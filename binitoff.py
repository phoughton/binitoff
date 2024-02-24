import uuid
import socket
from flask import jsonify, Flask, send_file, request
import os


# A flask server that will accept image data via a POST request
# It will then store those images locally and server them up when
# a request is made to the server

app = Flask(__name__)
port = 5000


@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['file']
    image_id = str(uuid.uuid4())
    image.save('images/' + f"{image_id}.png")
    file = f"{image_id}.png"
    return jsonify(filename=f"{image_id}.png",
                   url=f"http://{socket.gethostname()}:{port}/image/{file}")


@app.route('/image/<image_id>', methods=['GET'])
def get_image(image_id):

    return send_file('images/' + image_id, mimetype='image/png')


@app.route('/images', methods=['GET'])
def list_images():
    images = os.listdir('images')
    return jsonify(images=images)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
