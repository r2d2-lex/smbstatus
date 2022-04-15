from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class SearchForm(FlaskForm):
    sort_type = RadioField('sort_type', choices=[('sort_filename', 'Сортировка по имени файла/папки'),
                                                 ('sort_username', 'Сортировка по имени пользователя'),
                                                 ('sort_share', 'Сортировка по имени ресурса')],
                           coerce=str, validators=[DataRequired()], default='sort_filename')
    username = StringField('Имя пользователя:', id='username', render_kw={"class": "form-control"})
    filename = StringField('Имя файла/папки:', id='filename', render_kw={"class": "form-control"})
