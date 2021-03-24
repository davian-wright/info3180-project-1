from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf.csrf import CSRFProtect


class NewPropertiesForm(FlaskForm):
    title = TextField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    noofrooms = TextField('No. of Rooms', validators=[DataRequired()])
    noofbathrooms = TextField('No. of Bathrooms', validators=[DataRequired()])
    price = TextField('price', validators=[DataRequired()])
    propertytype = SelectField(u'Property Type', choices=[('house', 'house'),('apartment', 'apartment')])
    location = TextField('Location', validators=[DataRequired()])
    photo= FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only')])

   # submit = SubmitField('Submit')
   
   
   # addproperty=SubmitField()

