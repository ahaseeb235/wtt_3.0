from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, Optional

class UserInputForm(FlaskForm):
    id = IntegerField('ID', validators=[Optional()], render_kw={"readonly": True}) 
    name = StringField('Employee Name', validators=[DataRequired()])
    time_in = TimeField('Time In', validators=[Optional()])
    time_out = TimeField('Time Out', validators=[Optional()])
    month = SelectField('Month', choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])
    date = DateField('Date', validators=[DataRequired()])
    workday_type = SelectField('Workday Type', choices=[('Worked', 'Worked'), ('Training', 'Training'), ('Bank Holiday', 'Bank Holiday'), ('Annual Leave', 'Annual Leave'), ('Sick Leave', 'Sick Leave'), ('Overtime', 'Overtime') ])
    submit = SubmitField('Submit')
 
