from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, DateField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Optional
import re #importing regular expression module


class UserInputForm(FlaskForm):
    id = IntegerField('ID', validators=[Optional()], render_kw={"readonly": True}) 
    name = StringField('Employee Name', validators=[DataRequired()])
    time_in = TimeField('Time In', validators=[Optional()])
    time_out = TimeField('Time Out', validators=[Optional()])
    month = SelectField('Month', choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])
    date = DateField('Date', validators=[DataRequired()])
    workday_type = SelectField('Workday Type', choices=[('Worked', 'Worked'), ('Training', 'Training'), ('Bank Holiday', 'Bank Holiday'), ('Annual Leave', 'Annual Leave'), ('Sick Leave', 'Sick Leave'), ('Overtime', 'Overtime') ])
    submit = SubmitField('Submit')


# Custom validation method for the name field
    def validate_name(form, field):
        if not re.match("^[A-Za-z ]+$", field.data):
            raise ValidationError('Name must contain only letters and spaces.') 
