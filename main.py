import time
from flask import Flask, render_template, url_for, request, redirect,make_response, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import os

	# dd i nn iii

	
def i_to_state(i):
	return ["antra naktine", " pirma laisva", "antra laisva", "trecia laisva", "pirma dienine","antra dienine", "laisva diena", "pirma naktine"][i] 
	
def i_to_color(i):
	return [(255,0,0), (166,255,77), (77,255,77), (51,255,51), (210,255,77), (255,210,77), (255,153,51), (255,77,77)][i]
	
def work():
	h = 2 *60*60
	i = ( int(time.time()) + (h*60*60) ) // (60 * 60 * 24) % 8
	
	# print(i_to_state(i), i_to_color(i))
	return(i_to_state(i), i_to_color(i))



app = Flask(__name__)

@app.route("/")
def main():
	state, color = work()
	return render_template("base.html",w_state=state,w_color=color)
	
	
if __name__=="__main__":
	app.run(debug=False, host="0.0.0.0", port=80 , threaded=True)






main()

































