from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class SearchForm(FlaskForm):
    sort_type = RadioField('sort_type', choices=[('sort_filename', 'sort_filename'), ('sort_username', 'sort_username'),
                                                 ('sort_share', 'sort_share')], coerce=str, validators=[DataRequired()])
    username = StringField('Имя пользователя')
    filename = StringField('Имя файла/папки')
