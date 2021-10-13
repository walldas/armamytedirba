import time
from flask import Flask, render_template, url_for, request, redirect,make_response, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime#,date
import os
import ephem

	# dd i nn iii
	# location = {'longitude':24.4004631,'latitude': 56.0607279}
	
def add_moon_phases(days):

	date = datetime.now()
	
	f =  [1,ephem.next_full_moon(date).triple()[1],int(ephem.next_full_moon(date).triple()[2])]
	f2 = [1,ephem.previous_full_moon(date).triple()[1],int(ephem.previous_full_moon(date).triple()[2])]
	p =  [2,ephem.next_first_quarter_moon(date).triple()[1],int(ephem.next_first_quarter_moon(date).triple()[2])]
	p2 = [2,ephem.previous_first_quarter_moon(date).triple()[1],int(ephem.previous_first_quarter_moon(date).triple()[2])]
	j =  [3,ephem.next_new_moon(date).triple()[1],int(ephem.next_new_moon(date).triple()[2])]
	j2 = [3,ephem.previous_new_moon(date).triple()[1],int(ephem.previous_new_moon(date).triple()[2])]
	d =  [4,ephem.next_last_quarter_moon(date).triple()[1],int(ephem.next_last_quarter_moon(date).triple()[2])]
	d2 = [4,ephem.previous_last_quarter_moon(date).triple()[1],int(ephem.previous_last_quarter_moon(date).triple()[2])]
	moon_phases = [p,f,d,j,p2,f2,d2,j2]
	
	for moon in moon_phases:
		for day in days:
			if day[1] == moon[2] and day[3] == moon[1]:
				if moon[0]>0:
					day[4] = moon[0]
				break
				
	# print("1/4",ephem.next_first_quarter_moon(date))
	# print("full",ephem.next_full_moon(date))
	# print("3/4",ephem.next_last_quarter_moon(date))
	# print("new",ephem.next_new_moon(date))
	
	
	# return days

	
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
		month = int(datetime.fromtimestamp(dd).strftime('%m'))
		week= datetime.fromtimestamp(dd).isoweekday() - 1
		i = dd // (60 * 60 * 24) % 8
		moon = ""
		days.append([week, day, i_to_border_color(i),month, moon])
	add_moon_phases(days)
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
	n_weeks = []
	n_week=[]
	wkdays = ["P","A","T","K","Pe","Š","S"]
	wkdays = [[0,wk,(0,255,0,0)] for wk in wkdays]
	i = 0
	while i <7:
		n_week.append(wkdays[i])
		for week in weeks:
			n_week.append(week[i])
		n_weeks.append(n_week)
		n_week=[]
		i+=1
		
	return n_weeks
	
	
def work():
	h = 2 *60*60
	i = ( int(time.time()) + (h*60*60) ) // (60 * 60 * 24) % 8
	return(i_to_state(i), i_to_color(i))



app = Flask(__name__)

@app.route("/")
def index():
	weeks = to_table()
	state, color = work()
	return render_template("base.html",w_state=state,w_color=color,weeks=weeks)
	
@app.errorhandler(404)
def not_found(e):
	return index()


if __name__=="__main__":
	app.run(debug=1, host="0.0.0.0", port=5000 , threaded=True)

