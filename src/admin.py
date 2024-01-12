import os
from flask_admin import Admin
from models import db, Users, Profiles, Address, Planets, Characters #1. First we need to import the tables we want
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    #2. Create a view: Add your models here, for example this is how we add the User model to the admin
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Profiles, db.session))
    admin.add_view(ModelView(Address, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Characters, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))