from flask import render_template, flash, session, redirect, url_for, current_app

from . import main
from ..models import UnderclassPreorder, RequestInfo, RenewedContract, PhotoClass, GraduateCardOrder
from forms import UnderclassPreorderForm, RequestInfoForm, RenewContractForm, PhotoClassForm, GraduateCardOrderForm
from helpers import flash_errors

@main.route('/')
def index():
	return render_template('main/index.html')

@main.route('/enter_password')
def enter_password():
	return render_template('main/enter_password.html')

@main.route('/underclass_preorder', methods=['GET', 'POST'])
def underclass_preorder():
	form = UnderclassPreorderForm()
	if form.validate_on_submit():
		underclass_preorder = UnderclassPreorder(
				school=form.school.data,
				student_name=form.student_name.data,
				grade=form.grade.data,
				homeroom=form.homeroom.data,
				sport_name=form.sport_name.data,
				jersey_number=form.jersey_number.data,
				level=form.level.data,
				parent_name=form.parent_name.data,
				address=form.address.data,
				city=form.city.data,
				state=form.state.data,
				zipcode=form.zipcode.data,
				phone=form.phone.data,
				email=form.email.data,
				card_type=form.card_type.data,
				card_number=form.card_number.data,
				expiration_date=form.expiration_date.data,
				verification_code=form.verification_code.data,
				item_1=form.item_1.data,
				item_1_price=form.item_1_price.data,
				item_2=form.item_2.data,
				item_2_price=form.item_2_price.data,
				item_3=form.item_3.data,
				item_3_price=form.item_3_price.data,
				item_4=form.item_4.data,
				item_4_price=form.item_4_price.data
			)
		underclass_preorder.add()
		return redirect(url_for('main.underclass_preorder'))
	return render_template('main/underclass_preorder.html', form=form)

@main.route('/school_event_photos')
def school_event_photos():
	return render_template('main/school_event_photos.html')

@main.route('/admin_access')
def admin_access():
	return render_template('main/admin_access.html')

@main.route('/make_payment')
def make_payment():
	return render_template('main/make_payment.html')

@main.route('/administrator')
def administrator():
	return render_template('main/administrator.html')

@main.route('/interested_school', methods=['GET', 'POST'])
def interested_school():
	form = RequestInfoForm()
	if form.validate_on_submit():
		request_info = RequestInfo(
				name=form.name.data,
				organization=form.organization.data,
				position=form.position.data,
				address=form.address.data,
				city=form.city.data,
				state=form.state.data,
				zipcode=form.zipcode.data,
				phone=form.phone.data,
				email=form.email.data,
				current_photog=form.current_photog.data,
				comments_questions=form.comments_questions.data
			)
		request_info.add()
		return redirect(url_for('main.interested_school'))
	return render_template('main/interested_school.html', form=form)

@main.route('/retainer_school')
def retained_school():
	return render_template('main/retained_school.html')

@main.route('/information_sheet')
def information_sheet():
	return render_template('main/information_sheet.html')

@main.route('/renew_contract', methods=['GET', 'POST'])
def renew_contract():
	form = RenewContractForm()
	if form.validate_on_submit():
		renewed_contract = RenewedContract(
				as_outlined=form.as_outlined.data,
				e_signature=form.e_signature.data,
				seventeen_eighteen=form.seventeen_eighteen.data,
				eighteen_nineteen=form.eighteen_nineteen.data,
				nineteen_twenty=form.nineteen_twenty.data,
				additional_requests=form.additional_requests.data,
				school=form.school.data,
				address=form.address.data,
				city=form.city.data,
				state=form.state.data,
				zipcode=form.zipcode.data,
				phone=form.phone.data,
				email=form.email.data,
				comments_questions=form.comments_questions.data
			)
		renewed_contract.add()
		return redirect(url_for('main.renew_contract'))
	return render_template('main/renew_contract.html', form=form)

@main.route('/drug_free')
def drug_free():
	return render_template('main/drug_free.html')

@main.route('/non_collusion')
def non_collusion():
	return render_template('main/non_collusion.html')

@main.route('/non_descrimination')
def non_descrimination():
	return render_template('main/non_descrimination.html')

@main.route('/insurance')
def insurance():
	return render_template('main/insurance.html')

@main.route('/sexual_harassment')
def sexual_harassment():
	return render_template('main/sexual_harassment.html')

@main.route('/background_check')
def background_check():
	return render_template('main/background_check.html')

@main.route('/seniors')
def seniors():
	return render_template('main/seniors.html')

@main.route('/deluxe_session')
def deluxe_session():
	return render_template('main/deluxe_session.html')

@main.route('/standard_session')
def standard_session():
	return render_template('main/standard_session.html')
	
@main.route('/yearbook_session')
def yearbook_session():
	return render_template('main/yearbook_session.html')

@main.route('/family_session')
def family_session():
	return render_template('main/family_session.html')

@main.route('/location_session')
def location_session():
	return render_template('main/location_session.html')

@main.route('/faq')
def faq():
	return render_template('main/faq.html')

@main.route('/senior_products')
def senior_products():
	return render_template('main/senior_products.html')

@main.route('/graduate_card_order', methods=['GET', 'POST'])
def graduate_card_order():
	form = GraduateCardOrderForm()
	if form.validate_on_submit():
		grad_card_order = GraduateCardOrder(
				school=form.school.data,
				student_name=form.student_name.data,
				parent_name=form.parent_name.data,
				address=form.address.data,
				city=form.city.data,
				state=form.state.data,
				zipcode=form.zipcode.data,
				phone=form.phone.data,
				email=form.email.data,
				quantity=form.quantity.data,
				image_type=form.image_type.data,
				card_type=form.card_type.data,
				card_number=form.card_number.data,
				expiration_date=form.expiration_date.data,
				verification_code=form.verification_code.data,
				layout=form.layout.data,
				background_color=form.background_color.data,
				font=form.font.data,
				font_color=form.font_color.data,
				image_border=form.image_border.data,
				imprinting=form.imprinting.data,
				promo_code=form.promo_code.data,
				password=form.password.data,
				pose_number=form.pose_number.data
			)
		grad_card_order.add()
		return redirect('main.graduate_card_order')
	return render_template('main/graduate_card_order.html', form=form)

@main.route('/photo_collage')
def photo_collage():
	return render_template('main/photo_collage.html')

@main.route('/portraits')
def portraits():
	return render_template('main/portraits.html')

@main.route('/prekto11')
def prekto11():
	return render_template('main/prekto11.html')

@main.route('/directions')
def directions():
	return render_template('main/directions.html')

@main.route('/history')
def history():
	return render_template('main/history.html')

@main.route('/services')
def services():
	return render_template('main/services.html')

@main.route('/commercial')
def commercial():
	return render_template('main/commercial.html')

@main.route('/dance')
def dance():
	return render_template('main/dance.html')

@main.route('/sports')
def sports():
	return render_template('main/sports.html')

@main.route('/photo_class', methods=['GET', 'POST'])
def photo_class():
	form = PhotoClassForm()
	if form.validate_on_submit():
		photo_class = PhotoClass(
				name=form.name.data,
				address=form.address.data,
				city=form.city.data,
				state=form.state.data,
				zipcode=form.zipcode.data,
				phone=form.phone.data,
				email=form.email.data
			)
		photo_class.add()
		return redirect(url_for('main.photo_class'))
	return render_template('main/photo_class.html', form=form)

@main.route('/remove')
def remove():
	return render_template('main/remove.html')

@main.route('/request_info', methods=['GET', 'POST'])
def request_info():
	form = RequestInfoForm()
	if form.validate_on_submit():
		request_info = RequestInfo(
				name=form.name.data,
				organization=form.organization.data,
				position=form.position.data,
				address=form.address.data,
				city=form.city.data,
				state=form.state.data,
				zipcode=form.zipcode.data,
				phone=form.phone.data,
				email=form.email.data,
				current_photog=form.current_photog.data,
				comments_questions=form.comments_questions.data
			)
		request_info.add()
		return redirect(url_for('main.index'))
	return render_template('main/request_info.html', form=form)

	