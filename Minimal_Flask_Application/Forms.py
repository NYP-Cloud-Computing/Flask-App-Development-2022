from wtforms import Form, validators, StringField, RadioField, IntegerField, SelectField


class PersonForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100), validators.DataRequired()])

    country = SelectField('Country', [validators.DataRequired()], choices=[('', 'Select'), ('SG', 'Singapore'), ('M', 'Malaysia')], default='')

    industry = RadioField('Industry', choices=[('T', 'Technology'), ('E', 'Engineering'), ('H', 'Healthcare')], default='T')

    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')

