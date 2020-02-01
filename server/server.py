from flask import Flask, jsonify

from DB.connect import get_db
from constants import CONSTANTS

db = get_db()

app = Flask(__name__, static_folder='build')


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': 'hi'})


if __name__ == '__main__':
    app.run(port=CONSTANTS['PORT'])
