from nutri import db

class Food(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True, nullable=False)
	image_file = db.Column(db.String(50), unique=True, nullable=False, default='default.jpg')
	cal_per_unit = db.Column(db.Integer)
	protein_per_unit = db.Column(db.Integer)
	fat_per_unit = db.Column(db.Integer)
	carb_per_unit = db.Column(db.Integer)
	chosen = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return f"Food('{self.name}','{self.image_file}','{self.cal_per_unit}','{self.protein_per_unit}','{self.fat_per_unit}','{self.carb_per_unit}','{self.chosen}')"
