from flask import Blueprint,url_for,redirect

bp = Blueprint('main',__name__)

@bp.route('/')
def index():
    return redirect(url_for('question.list'))

