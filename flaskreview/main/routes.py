from flask import Blueprint, request, render_template
from flaskreview.models import Review, User
from flask_restful import  Resource, abort, fields, marshal_with


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.order_by(Review.date_created.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', reviews=reviews)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


