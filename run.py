#!/usr/bin/python

from flask import Flask, request, render_template
import main

app = Flask(__name__)
app.debug = True

global wh_code
wh_code = None
global wh_result 
wh_result = None
global ship_count 
ship_count = None

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if 'initialize' in request.form:
			global wh_code
			wh_code = request.form['wh_code']
			global wh_result
			wh_result = main.wh_info(wh_code)
			return render_template('index2.html', wh_result=wh_result)
		if 'roll_count' in request.form:
			global ship_count 
			ship_count = request.form['ship_count']
			return render_template('index3.html', ship_count=ship_count, wh_result=wh_result)
		if 'final_calc' in request.form:
			params = [ [i+j for j in range(3)] for i in range(int(ship_count))]
			for i in range(0, int(ship_count)):
				params[i][0] = request.form['Name'+str(i)]
				params[i][1] = request.form['Mass'+str(i)]
				params[i][2] = request.form['Mwd'+str(i)]
			final_result = main.wh_calc(wh_code, params)
			return render_template('index4.html', wh_result=wh_result, final_result=final_result)
	return render_template('index1.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
