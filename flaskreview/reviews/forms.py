from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ReviewForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    rating = IntegerField('Rating', validators = [DataRequired(), NumberRange(min=1, max=10)])
    description = TextAreaField('Description', validators=[DataRequired()])
    #picture = FileField('Add Pictures', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Add Review')