from flask import Flask, render_template, request, redirect, url_for
from Form import PersonForm
import shelve, Person
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

csrf = CSRFProtect(app)

app.secret_key = 'dnjkbjwfbiewnfkjensjebnjskbkdsjbcfsejkbsjkbwebfsibncskjcbcvubesbgcshce'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/createperson', methods=['GET', 'POST'])
def create_person():
    person_form = PersonForm(request.form)
    if request.method == 'POST' and person_form.validate():

        person_dict = {}
        db = shelve.open('person.db', 'c')

        try:
            person_dict = db['Person']
        except:
            print("Error in retrieving Person from person.db.")

        email = person_form.email.data
        password = person_form.password.data
        person = Person.Person(email, password)

        person_dict[person.get_uid()] = person
        db['Person'] = person_dict

        # Test codes
        person_dict = db['Person']
        person = person_dict[person.get_uid()]
        print("Person's UID:", person.get_uid(), ", "
              "Person's Email:", person.get_email(), ", "
              "Person Password:", person.get_password())

        return redirect(url_for('home'))
    return render_template('createperson.html', form=person_form)


if __name__ == '__main__':
    app.run(host="127.0.0.2", port=8080, debug=True)






