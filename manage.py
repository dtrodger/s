#!/usr/bin/env python
import os
from app import create_app, db
from app.models import UnderclassPreorder, RequestInfo, RenewedContract, PhotoClass, GraduateCardOrder
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

admin = Admin(app)
admin.add_view(ModelView(UnderclassPreorder, db.session))
admin.add_view(ModelView(RequestInfo, db.session))
admin.add_view(ModelView(RenewedContract, db.session))
admin.add_view(ModelView(PhotoClass, db.session))
admin.add_view(ModelView(GraduateCardOrder, db.session))
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
	return dict(app=app, db=db)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_option('-a', '--app', dest='application', default='demo')
manager.add_option('-c', '--config', dest='config', default='default')
# manager.add_command("runserver", Server(use_reloader=True))

if __name__ == '__main__':
	manager.run()