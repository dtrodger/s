import datetime

from . import db
from mixins.db_mixins import DBOppMixin


class UnderclassPreorder(DBOppMixin, db.Model):
	__tablename__ = 'underclass_preorders'
	id = db.Column(db.Integer, primary_key=True)
	school = db.Column(db.String(64))
	student_name = db.Column(db.String(64))
	grade = db.Column(db.String(64))
	homeroom = db.Column(db.String(64))
	sport_name = db.Column(db.String(64))
	jersey_number = db.Column(db.String(64))
	level = db.Column(db.String(64))
	parent_name = db.Column(db.String(64))
	address = db.Column(db.String(64))
	city = db.Column(db.String(64))
	state = db.Column(db.String(64))
	zipcode = db.Column(db.String(64))
	phone = db.Column(db.String(64))
	email = db.Column(db.String(64))
	card_type = db.Column(db.String(64))
	card_number = db.Column(db.String(64))
	expiration_date = db.Column(db.String(64))
	verification_code = db.Column(db.String(64))
	item_1 = db.Column(db.String(64))
	item_1_price = db.Column(db.String(64))
	item_2 = db.Column(db.String(64))
	item_2_price = db.Column(db.String(64))
	item_3 = db.Column(db.String(64))
	item_3_price = db.Column(db.String(64))
	item_4 = db.Column(db.String(64))
	item_4_price = db.Column(db.String(64))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __init__(self, **kwargs):
		super(UnderclassPreorder, self).__init__(**kwargs)
		self.created = datetime.datetime.now()
		self.updated = datetime.datetime.now()

	def __repr__(self):
		return '<Underclass Preorder %r>' % self.id


class RequestInfo(DBOppMixin, db.Model):
	__tablename__ = 'information_requests'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	organization = db.Column(db.String(64))
	position = db.Column(db.String(64))
	address = db.Column(db.String(64))
	city = db.Column(db.String(64))
	state = db.Column(db.String(64))
	zipcode = db.Column(db.String(64))
	phone = db.Column(db.String(64))
	email = db.Column(db.String(64))
	current_photog = db.Column(db.String(64))
	comments_questions = db.Column(db.String(256))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __init__(self, **kwargs):
		super(RequestInfo, self).__init__(**kwargs)
		self.created = datetime.datetime.now()
		self.updated = datetime.datetime.now()

	def __repr__(self):
		return '<Requested Information %r>' % self.id


class RenewedContract(DBOppMixin, db.Model):
	__tablename__ = 'renewed_contracts'
	id = db.Column(db.Integer, primary_key=True)
	as_outlined = db.Column(db.Boolean)
	e_signature = db.Column(db.String(64))
	seventeen_eighteen = db.Column(db.Boolean)
	eighteen_nineteen = db.Column(db.Boolean)
	nineteen_twenty = db.Column(db.Boolean)
	additional_requests = db.Column(db.String(256))
	school = db.Column(db.String(64))
	address = db.Column(db.String(64))
	city = db.Column(db.String(64))
	state = db.Column(db.String(64))
	zipcode = db.Column(db.String(64))
	phone = db.Column(db.String(64))
	email = db.Column(db.String(64))
	comments_questions = db.Column(db.String(256))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __init__(self, **kwargs):
		super(RenewedContract, self).__init__(**kwargs)
		self.created = datetime.datetime.now()
		self.updated = datetime.datetime.now()

	def __repr__(self):
		return '<Renewed Contract %r>' % self.id


class PhotoClass(DBOppMixin, db.Model):
	__tablename__ = 'photo_classes'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	address = db.Column(db.String(64))
	city = db.Column(db.String(64))
	state = db.Column(db.String(64))
	zipcode = db.Column(db.String(64))
	phone = db.Column(db.String(64))
	email = db.Column(db.String(64))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __init__(self, **kwargs):
		super(PhotoClass, self).__init__(**kwargs)
		self.created = datetime.datetime.now()
		self.updated = datetime.datetime.now()

	def __repr__(self):
		return '<Photo Class Request %r>' % self.id


class GraduateCardOrder(DBOppMixin, db.Model):
	__tablename__ = 'grad_card_orders'
	id = db.Column(db.Integer, primary_key=True)
	school = db.Column(db.String(64))
	student_name = db.Column(db.String(64))
	parent_name = db.Column(db.String(64))
	address = db.Column(db.String(64))
	city = db.Column(db.String(64))
	state = db.Column(db.String(64))
	zipcode = db.Column(db.String(64))
	phone = db.Column(db.String(64))
	email = db.Column(db.String(64))
	quantity = db.Column(db.String(64))
	image_type = db.Column(db.String(64))
	card_type = db.Column(db.String(64))
	card_number = db.Column(db.String(64))
	expiration_date = db.Column(db.String(64))
	verification_code = db.Column(db.String(64))
	layout = db.Column(db.String(64))
	background_color = db.Column(db.String(64))
	font = db.Column(db.String(64))
	font_color = db.Column(db.String(64))
	image_border = db.Column(db.String(64))
	imprinting = db.Column(db.String(256))
	promo_code = db.Column(db.String(64))
	password = db.Column(db.String(64))
	pose_numeber = db.Column(db.String(64))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __init__(self, **kwargs):
		super(GraduateCardOrder, self).__init__(**kwargs)
		self.created = datetime.datetime.now()
		self.updated = datetime.datetime.now()

	def __repr__(self):
		return '<Grad Card Order %r>' % self.id
