from flask import Flask, jsonify

from constants import CONSTANTS

app = Flask(__name__, static_folder='build')


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': 'hi'})


if __name__ == '__main__':
    app.run(port=CONSTANTS['PORT'])
