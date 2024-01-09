from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, BooleanField

class CreateNewRating(FlaskForm):
    stars = SelectField(
        choices=[(i, i) for i in range(1, 6)],
        render_kw={'style': 'font-size: 18px;'},
        coerce=int
    )
    grade = SelectField(
        choices=[("A", "A"), ("A-", "A-"), ("B+", "B+"), ("B", "B"), ("B-", "B-"), ("C+", "C+"), ("C", "C"),
                 ("C-", "C-"), ("D+", "D+"), ("D", "D"), ("F", "F")],
        render_kw={'style': 'font-size: 18px;'}
    )
    difficulty = SelectField(
        choices=[(i, i) for i in range(1, 6)],
        render_kw={'style': 'font-size: 18px;'},
        coerce=int
    )
    comment = TextAreaField(
        render_kw={'rows': 5, 'cols': 40, 'style': 'font-family: Montserrat; font-size: 18px; color: rgb(0, 0, 139);'}
    )
    anonymous = BooleanField()