from models import User, Message
from extensions import app, db

with app.app_context():

    db.create_all()