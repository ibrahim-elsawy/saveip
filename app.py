from flask import Flask, request, jsonify, Response
import os
from waitress import serve
from middleware import HandleRequest

import os
os.environ['ENV'] = 'production'

app = Flask(__name__)

# PORT = os.environ.get("PORT")

@app.route("/ip", methods=['POST'])
def postIP():
	if request.method == 'POST':
		try:
			req = request.get_json()
			handler = HandleRequest()
			status_code = handler.ip_post(req)
			return Response(status = status_code)
		except Exception as e:
			return 400


@app.route("/ip", methods=['GET'])
def getIP():
	if request.method == 'GET':
		try:
			# req = request.get_json()
			handler = HandleRequest()
			res = handler.ip_get()
			return jsonify(res)
		except Exception as e:
			return 400




			
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000)) 
	# app.run(app, port=port)
	serve(app, host="0.0.0.0", port=PORT) 
