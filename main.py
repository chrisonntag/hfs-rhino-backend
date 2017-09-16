import sys
import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Rhino.'


@app.route('/update', methods=['POST'])
def update():
    try:
        lat = request.form['latitude']
        lng = request.form['longitude']
        return jsonify({'lat': lat, 'lng': lng})
    except Exception as ex:
        return jsonify({'error': str(ex), 'trace': traceback.format_exc()})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    app.run(host='127.0.0.1', port=port, debug=True)
