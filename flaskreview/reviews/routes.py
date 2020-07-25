from flask import Blueprint, render_template, abort, redirect, url_for, flash, request, current_app
from flaskreview.reviews.forms import ReviewForm
from flaskreview.models import Review
from flaskreview import db
from flask_login import current_user, login_required

reviews = Blueprint('reviews', __name__)


@reviews.route('/review/new', methods=['GET', 'POST'])
@login_required
def new_review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(title=form.title.data, description=form.description.data,
                        rating=form.rating.data, author=current_user)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_review.html', title='Add Review', form=form, header='Add Review')


@reviews.route('/review/<int:review_id>')
def review(review_id):
    review = Review.query.get_or_404(review_id)
    return render_template('review.html', title='Review', header='Review', review=review)


@reviews.route('/review/<int:review_id>/update', methods=['GET', 'POST'])
@login_required
def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.author != current_user:
        abort(403)
    form = ReviewForm()
    if form.validate_on_submit():
        review.title = form.title.data
        review.rating = form.rating.data
        review.description = form.description.data
        db.session.commit()
        flash('Your review has been updated', 'success')
        return redirect(url_for('reviews.review', review_id=review.id))
    elif request.method == 'GET':
        form.title.data = review.title
        form.rating.data = review.rating
        form.description.data = review.description
    return render_template('create_review.html', title='Update Review', header='Update Review', form=form)


@reviews.route('/review/<int:review_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.author != current_user:
        abort(403)
    db.session.delete(review)
    db.session.commit()
    flash('Your review has been deleted', 'success')
    return redirect(url_for('main.home'))