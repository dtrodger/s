from flask_wtf import Form, widgets
from wtforms import StringField, BooleanField, SelectField, SelectMultipleField, IntegerField, SubmitField, TextField
from wtforms.widgets import TextArea
from wtforms.validators import Required, Length, Email, Regexp, EqualTo


GRADE_CHOICES = [
		('JK', 'JK'),
		('K', 'K'),
		('1st', '1st'),
		('2nd', '2nd'),
		('3rd', '3rd'),
		('4th', '4th'),
		('5th', '5th'),
		('6th', '6th'),
		('7th', '7th'),
		('8th', '8th'),
		('9th', '9th'),
		('10th', '10th'),
		('11th', '11th'),
		('12th', '12th')
	]

SPORT_LEVELS = [
		('Varsity', 'Varsity'),
		('Junior Varisty', 'Junior Varisty'),
		('Sophomore', 'Sophomore'),
		('Freshman', 'Freshman'),
		('Other', 'Other')
	]

CARD_TYPES = [
		('Visa', 'Visa'),
		('Master Card', 'Master Card'),
		('American Express', 'American Express'),
		('Discover Card', 'Discover Card')
	]

GRAD_CARD_LAYOUTS = [
		('Layout A', 'A'),
		('Layout B', 'B'),
		('Layout C', 'C'),
		('Layout D', 'D'),
		('Layout E', 'E'),
		('Layout F', 'F'),
		('Layout G', 'G'),
		('Layout H', 'H'),
		('Layout I', 'I'),
		('Layout J', 'J'),
		('Layout K', 'K'),
		('Layout L', 'L')
	]

GRAD_CARD_COLORS = [
		('Black', 'Black'),
		('Blue', 'Blue'),
		('Brown', 'Brown'),
		('Coral', 'Coral'),
		('Dark Blue', 'Dark Blue'),
		('Dark Green', 'Dark Green'),
		('Gold', 'Gold'),
		('Grey', 'Grey'),
		('Light Blue', 'Light Blue'),
		('Light Green', 'Light Green'),
		('Maroon', 'Maroon'),
		('Orange', 'Orange'),
		('Purple', 'Purple'),
		('Red', 'Red'),
		('Royal Blue', 'Royal Blue'),
		('Tan Texture', 'Tan Texture'),
		('White', 'White'),
		('Yellow', 'Yellow')
	]

GRAD_CARD_QUANTITIES = [
		('25 for $95', '25 for $95'),
		('50 for $158', '50 for $158'),
		('75 for $190', '75 for $190'),
		('100 for $225', '100 for $225')
	]

GRAD_CARD_IMAGE_TYPES = [
		('Color', 'Color'),
		('Black and White', 'Black and White')
	]

GRAD_CARD_FONTS = [
		('Same as Sample', 'Same as Sample'),
	  	('Algerian', 'Algerian'),
	  	('Amazone', 'Amazone'),
	  	('Aparajita', 'Aparajita'),
	  	('Bradley Hand', 'Bradley Hand'),
	  	('Brush Script', 'Brush Script'),
	  	('Candara', 'Candara'),
	  	('Century Gothic', 'Century Gothic'),
	  	('Chaparral Pro', 'Chaparral Pro'),
	  	('Corel', 'Corel'),
	  	('Coronet', 'Coronet'),
	  	('Desdemona', 'Desdemona'),
	  	('Eccentric STD', 'Eccentric STD'),
	  	('Edwardian Script', 'Edwardian Script'),
	  	('Fifth Ave', 'Fifth Ave'),
	  	('Footlight MT Light', 'Footlight MT Light'),
	  	('Future', 'Future'),
	  	('Impact', 'Impact'),
	  	('Kinn MT', 'Kinn MT'),
	  	('Minion Pro', 'Minion Pro'),
	  	('Optima', 'Optima'),
	  	('ProvLite', 'ProvLite'),
	  	('Segoe Script', 'Segoe Script'),
	  	('Sirona', 'Sirona'),
	  	('Technical', 'Technical')
  	]

GRAD_CARD_IMAGE_BORDERS = [
		('None', 'None'),
		('Artistic Edge', 'Artistic Edge'),
		('Line', 'Line')
	]


class UnderclassPreorderForm(Form):
	school = StringField('School', validators=[Required()])
	student_name = StringField('Student Name', validators=[Required()])
	grade = SelectField('Grade', choices=GRADE_CHOICES, validators=[Required()])
	homeroom = StringField('Homeroom', validators=[Required()])
	sport_name = StringField('Sport Name')
	jersey_number = StringField('Jersey Number')
	level = SelectField('Level', choices=SPORT_LEVELS)
	parent_name = StringField('Parent Name', validators=[Required()])
	address = StringField('Address', validators=[Required()])
	city = StringField('City', validators=[Required()])
	state = StringField('State', validators=[Required()])
	zipcode = StringField('Zip Code', validators=[Required()])
	phone = StringField('Phone Number', validators=[Required()])
	email = StringField('Email', validators=[Required()])
	card_type = SelectField('Credit Card Type', choices=CARD_TYPES, validators=[Required()])
	expiration_date = StringField('Expiration Date', validators=[Required()])
	verification_code = StringField('Verification Code', validators=[Required()])
	item_1 = StringField('Item 1', validators=[Required()])
	item_1_price = StringField('Item 1 Price', validators=[Required()])
	item_2 = StringField('Item 2')
	item_2_price = StringField('Item 2 Price')
	item_3 = StringField('Item 3')
	item_3_price = StringField('Item 3 Price')
	item_4 = StringField('Item 4')
	item_4_price = StringField('Item 4 Price')
	submit = SubmitField('Submit Order')


class RequestInfoForm(Form):
	name = StringField('Name', validators=[Required()])
	organization = StringField('Organization', validators=[Required()])
	position = StringField('Position', validators=[Required()])
	address = StringField('Address', validators=[Required()])
	city = StringField('City', validators=[Required()])
	state = StringField('State', validators=[Required()])
	zipcode = StringField('Zip Code', validators=[Required()])
	phone = StringField('Phone Number', validators=[Required()])
	email = StringField('Email', validators=[Required()])
	current_photog = StringField('Current Photographer')
	comments_questions = TextField('Comments or Questions', widget=TextArea())
	submit = SubmitField('Submit')


class RenewContractForm(Form):
	as_outlined = BooleanField('I Agree to the Program as Outlined in Contract Terms')
	e_signature = StringField('Electronic Signature', validators=[Required()])
	seventeen_eighteen = BooleanField('2017-2018')
	eighteen_nineteen = BooleanField('2018-2019 $500 Signing Bonus')
	nineteen_twenty = BooleanField('2019-2020 $750 Signing Bonus')
	additional_requests = TextField('Additional Requests', widget=TextArea())
	school = StringField('School', validators=[Required()])
	address = StringField('Address', validators=[Required()])
	city = StringField('City', validators=[Required()])
	state = StringField('State', validators=[Required()])
	zipcode = StringField('Zip Code', validators=[Required()])
	phone = StringField('Phone Number', validators=[Required()])
	email = StringField('Email', validators=[Required()])
	comments_questions = TextField('Comments or Questions', widget=TextArea())
	submit = SubmitField('Submit')


class PhotoClassForm(Form):
	name = StringField('Name', validators=[Required()])
	address = StringField('Address')
	city = StringField('City')
	state = StringField('State')
	zipcode = StringField('Zip Code')
	phone = StringField('Phone Number')
	email = StringField('Email')
	submit = SubmitField('Submit')

# GET CC INFO?

class GraduateCardOrderForm(Form):
	school = StringField('School', validators=[Required()])
	student_name = StringField('Student Name', validators=[Required()])
	parent_name = StringField('Parent Name', validators=[Required()])
	address = StringField('Address', validators=[Required()])
	city = StringField('City', validators=[Required()])
	state = StringField('State', validators=[Required()])
	zipcode = StringField('Zip Code', validators=[Required()])
	phone = StringField('Phone Number', validators=[Required()])
	email = StringField('Email', validators=[Required()])
	quantity = SelectField('Quantity', choices=GRAD_CARD_QUANTITIES),
	image_type = SelectField('Image Type', choices=GRAD_CARD_IMAGE_TYPES),
	card_type = SelectField('Credit Card Type', choices=CARD_TYPES, validators=[Required()])
	card_number = StringField('Card Number', validators=[Required()])
	expiration_date = StringField('Expiration Date', validators=[Required()])
	verification_code = StringField('Verification Code', validators=[Required()])
	layout = SelectField('Layout', choices=GRAD_CARD_LAYOUTS, validators=[Required()])
	background_color = SelectField('Color', choices=GRAD_CARD_COLORS, validators=[Required()])
	font = SelectField('Font', choices=GRAD_CARD_FONTS, validators=[Required()])
	font_color = SelectField('Font Color', choices=GRAD_CARD_COLORS, validators=[Required()])
	image_border = SelectField('Image Border', choices=GRAD_CARD_IMAGE_BORDERS, validators=[Required()])
	imprinting = StringField('Card Imprinting', widget=TextArea())
	promo_code = StringField('Promo Code')
	password = StringField('Password', validators=[Required()])
	pose_number = StringField('Pose Number', validators=[Required()])
	submit = SubmitField('Submit Order')
