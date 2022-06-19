from enum import unique
from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Absensi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_in = db.Column(db.DateTime(timezone=True), default=func.now())
    check_out = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    username = db.Column(db.String(150), db.ForeignKey('user.username'))

class Aktivitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_aktivitas = db.Column(db.String(500))
    tgl_aktivitas = db.Column(db.Date(), default=func.current_date())
    waktu_aktivitas = db.Column(db.Time(), default=func.current_time(timezone=True))
    status = db.Column(db.String(150))
    username = db.Column(db.String(150), db.ForeignKey('user.username'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    aktivitas = db.relationship('Aktivitas')
    absensi = db.relationship('Absensi')