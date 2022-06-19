from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Absensi, Aktivitas
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        aktivitas = request.form.get('aktivitas')
        if len(aktivitas) < 1:
            flash('Aktivitas terlalu pendek!', category='error')
        else:
            new_aktivitas = Aktivitas(nama_aktivitas=aktivitas, username=current_user.username, status="on-going")
            db.session.add(new_aktivitas)
            db.session.commit()
            flash('Aktivias ditambahkan!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/update-aktivitas', methods=['POST'])
def update_aktivitas():
    if request.method == 'POST':
        status = Aktivitas.query.get(request.form.get('status'))
        status.name = "finished"
        db.session.commit()

    return render_template("home.html", user=current_user)

@views.route('/delete-aktivitas', methods=['POST'])
def delete_aktivitas():
    aktivitas = json.loads(request.data)
    IdAktivitas = aktivitas['IdAktivitas']
    aktivitas = Aktivitas.query.get(IdAktivitas)
    if aktivitas:
        if aktivitas.username == current_user.username:
            db.session.delete(aktivitas)
            db.session.commit()

    return jsonify({})