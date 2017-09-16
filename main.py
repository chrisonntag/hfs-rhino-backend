import sys
import traceback
from flask import Flask, request, jsonify
from controllers.theweathercompany import WeatherRegion
from controllers.knowledge import KnowledgeBase

app = Flask(__name__)
version = 'v1.0'
project_name = 'rhino'
pre = '/%s' % project_name


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Rhino.', 'version': version, 'base_url': '%s/' % pre})


@app.route('%s/update' % pre, methods=['POST'])
def update():
    try:
        lat = request.form['latitude']
        lng = request.form['longitude']
        region = WeatherRegion(lat, lng)

        if region.is_endangered():
            data = region.parse()
            db = KnowledgeBase()
            return jsonify({
                'endangered': True,
                'type': data['type'],
                'level': data['level'],
                'instructions': db.get_instructions(data)
            })
        else:
            return jsonify({'endangered': False})
    except Exception as ex:
        return jsonify({'error': str(ex), 'trace': traceback.format_exc()})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    app.run(host='127.0.0.1', port=port, debug=True)
