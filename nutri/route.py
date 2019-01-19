from flask import render_template, request, redirect, url_for
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
	food_l = Food.query.all()
	return render_template('index.html', food_l=food_l)

@app.route('/result', methods=['POST'])
def result():
	return render_template('result.html')

@app.route('/admin',methods=['GET', 'POST'])
def admin():
	return render_template('admin.html')