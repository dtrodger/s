from .. import db
from sqlalchemy.exc import SQLAlchemyError

class DBOppMixin:
	def add(self):
		db.session.add(self)
		return session_commit()

	def update(self):
		self.updated = datetime.datetime.now()
		return session_commit()

	def delete(self):
		db.session.delete(self)
		return session_commit()

def session_commit():
	try:
		db.session.commit()
	except SQLAlchemyError as e:
		db.session.rollback()
		reason=str(e)
		return reason
