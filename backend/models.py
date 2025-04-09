from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Sauna session model
class SaunaSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    notes = db.Column(db.Text)

    user = db.relationship("User", backref=db.backref("sessions", lazy=True))
