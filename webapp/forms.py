from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms.validators import InputRequired


class SearchForm(FlaskForm):
    sorting_type = RadioField('flexRadioSorting', choices=['flexRadioFilename', 'flexRadioUsername', 'flexRadioShare'],)
                              # validators=[InputRequired()])
