from flask import Flask
from flask import jsonify
from flask import request
import subprocess

app = Flask(__name__)

x_value = 0
y_value = 0

@app.route('/hello',methods=['POST'])
def hello():
	global x_value
	global y_value
	message = request.get_json(force=True)
	
	xval = int(message['xval']) if int(message['xval']) !=0 else x_value
	yval = int(message['yval']) if int(message['yval']) !=0 else y_value

	x_value = xval
	y_value = yval

	try:
		result = subprocess.check_output(
            ["python2","AE.py","--x",str(xval),"--y",str(yval)])
	except Exception:
		result = None
	print(result)
	response = {
		'greeting' : str(xval)+' , '+str(yval)
	}
	return jsonify(response)
   	
