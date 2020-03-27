from flask import Flask
import os
#dirs, in case I need them later- not in use currently
TEMPLATE_DIR = os.path.abspath('/app/templates')
STATIC_DIR = os.path.abspath('/app/static')

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'hhmmmm'



from app import views
from app import admin_views