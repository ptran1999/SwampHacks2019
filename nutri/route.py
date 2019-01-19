from flask import render_template, request
from nutri import app, db
from nutri.models import Food

@app.route('/')
def index():
	food_l = Food.query.all()
	return render_template('index.html', food_l=food_l)

@app.route('/result', methods=['POST'])
def result():
	return render_template('result.html')

@app.route('/admin')
def admin():
	name = request.form['Name']
	cal = request.form['cal']
	protein = request.form['protein']
	fat = request.form['fat']
	carb = request.form['carb']
	return render_template('admin.html')

