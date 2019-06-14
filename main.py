"""main.py

An example script for demoing swaggerui functionality with quart
"""
import os
from quart import Quart, request, flash, make_response
from quart_swagger_blueprint import swagger_ui

app = Quart(__name__)

@app.route('/hello_world', methods=['POST'])
async def hello_world():
    if request.method == 'POST':
        data = await request.get_json()
        # print(data)
        if data:
            if data.get('name'):
                text = "Hello World "+data["name"]
                response = await make_response(text, 200)
                return response
    response = await make_response("Bad Request", 400)   
    return response

# register the swaggerui display
app.register_blueprint(swagger_ui)

app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
