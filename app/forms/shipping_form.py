from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired
from map.map import map     # dicitonary of cities with values as the connected cities

cities = list(map.keys())   #get just the cities, no connections. to place in select field
#when passing into 'choices' for select field, if you choose to use a list of strings
# rather than a list of (value, text) tuples, then the string will be assigned
# to both the value and the text.

class Shipping(FlaskForm):
   sender = StringField('Sender', validators = [DataRequired()])
   recipient = StringField('Recipient', validators = [DataRequired()])
   origin = SelectField('Origin', choices = cities, validators = [DataRequired()])
   destination = SelectField('Destination', choices = cities, validators = [DataRequired()])
   express = BooleanField('Express Shipping')
   submit = SubmitField('Submit')
   cancel = SubmitField('Cancel')
