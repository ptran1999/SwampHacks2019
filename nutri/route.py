from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
import os
import requests
import json
from nutri import app, db
from nutri.models import Food

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		temp = Food(name=request.form['food_name'], 
				image_file=request.form['Image'], 
				cal_per_unit=request.form['cal'], 
				protein_per_unit=request.form['protein'], 
				fat_per_unit=request.form['fat'], 
				carb_per_unit=request.form['carb'])
		db.session.add(temp)
		db.session.commit()
	food_l = Food.query.filter_by(chosen=False).all()
	chosen = Food.query.filter_by(chosen=True).all()

	return render_template('index.html',food_l=food_l, chosen=chosen)

@app.route('/result', methods=['POST'])
def result(): 
	food_l = Food.query.filter_by(chosen=True).all()
	name_l =""
	for food in food_l:
		name_l += food.name +","
	response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=10&ranking=1&ingredients=" + name_l,
	headers=
		{
		"X-RapidAPI-Key": "s6HusAzP3HmshznEWUR6xxLqFEJip1th9jVjsnLjtd8NUEMj6d"
		}
	)
	arr=[]
	json_object = json.loads(response.text)
	for i in json_object:
		arr.append(i['title'])
	return render_template('result.html', arr=arr, food_l=food_l)


@app.route('/about',methods=['GET','POST'])
def about():
	return render_template('about.html')

@app.route('/admin',methods=['GET', 'POST'])
def admin():
	return render_template('login.html')
	
@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
		return render_template('admin.html')
	else:
		flash('wrong password or username')
		return render_template('login.html')
		
@app.route('/admin.html')
def logout():
	session['logged_in'] = False
	return home()

@app.route('/chosen/<id>')
def chosen(id):
	food = Food.query.filter_by(id=int(id)).first()
	food.chosen = True
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/remove/<id>')
def remove(id):
	food = Food.query.filter_by(id=int(id)).first()
	food.chosen = False
	db.session.commit()
	return redirect(url_for('index'))
	
