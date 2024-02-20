#!/usr/bin/env python3

"""
gunicorn --config './gunicorn.conf.py' app:app
"""

import json
from flask import Flask, jsonify, request
from paddlenlp import Taskflow
import logging

app = Flask(__name__)
logging.basicConfig(filename='console.log')

@app.route('/image/extract', methods = ['POST'])
def image():
    data = json.loads(request.get_data(as_text=True))
    image_url = data.get('image_url')
    schema = data.get('schema')
    
    if type(schema).__name__ != "list":
        logging.error("invalid schema: {}".format(schema))
        return jsonify({
            "error": "invalid schema"
        })
    
    try:
        ie = Taskflow("information_extraction", schema=schema, model="uie-x-base", layout_analysis=True)
        results = ie({"doc": image_url})
    except Exception as e:
        logging.error(str(e))
        return jsonify({
            "error": str(e)
        })
    
    info = []
    for result in results:
        for k, v in result.items():
            for vv in v:
                info.append({
                    'element': k,
                    'text': vv.get('text')
                })
    return jsonify({
        'info': info
    })
    
if __name__ == '__main__':
    with app.app_context():
        app.run()