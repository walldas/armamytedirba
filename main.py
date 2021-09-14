import time
from flask import Flask, render_template, url_for, request, redirect,make_response, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import os

	# dd i nn iii

	
def i_to_state(i):
	return ["antra naktinė", " pirma laisva", "antra laisva", "trečia laisva", "pirma dieninė","antra dieninė", "laisva diena", "pirma naktinė"][i] 
	
def i_to_color(i):
	return [(255,0,0), (166,255,77), (77,255,77), (51,255,51), (210,255,77), (255,210,77), (255,153,51), (255,77,77)][i]
	
def i_to_border_color(i):
	a=[1,1,0,2,2,0,0,0][i]
	return [(0,255,0,0),(255,255,255,1),(0,0,0,1)][a]

def to_table():
	days = []
	for d in range(0,31,1):
		dd = int(time.time() + d * 60 * 60 * 24)
		day = int(datetime.fromtimestamp(dd).strftime('%d'))
		week= datetime.fromtimestamp(dd).isoweekday() - 1
		i = dd // (60 * 60 * 24) % 8
		days.append([week,day,i_to_border_color(i)])
	weeks = []
	week =[]
	[week.append([wk,"",(0,255,0,0)]) for wk in range(days[0][0])]
	for day in days:
		if not len(week) == 7:
			week.append(day)
		else:
			weeks.append(week)
			week = [day]
	# if not len(week) == 7:
		# weeks.append(week)
		
		
	return weeks
	
	
def work():
	h = 2 *60*60
	i = ( int(time.time()) + (h*60*60) ) // (60 * 60 * 24) % 8
	return(i_to_state(i), i_to_color(i))



app = Flask(__name__)

@app.route("/")
def main():
	weeks = to_table()
	state, color = work()
	return render_template("base.html",w_state=state,w_color=color,weeks=weeks)
	
	
if __name__=="__main__":
	app.run(debug=False, host="0.0.0.0", port=5000 , threaded=True)






main()

































