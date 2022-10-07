from wtforms import Form, validators, EmailField, PasswordField


class PersonForm(Form):
    email = EmailField("Email", [validators.Email()])

    password = PasswordField("Password", [validators.length(8)])
