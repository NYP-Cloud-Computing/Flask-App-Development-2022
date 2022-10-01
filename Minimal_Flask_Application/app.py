from flask import Flask, render_template, request, redirect, url_for
from Forms import PersonForm
from flask_wtf.csrf import CSRFProtect
import shelve, Person

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = 'jiceuiruineruiferuifbwneionweicbuivbruinewicwebvuierniwndiwebciuevbiuerdniweoncueivbuiecbwuicbewui'


@app.route('/')
def home():
    return render_template('home.html')


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

        person = Person.Person(person_form.name.data, person_form.country.data, person_form.industry.data,
                               person_form.gender.data)

        person_dict[person.get_uid()] = person
        db['Person'] = person_dict

        # Test codes
        person_dict = db['Person']
        person = person_dict[person.get_uid()]
        print(person.get_name(), person.get_country(), person.get_industry(), person.get_gender())

        db.close()

        return redirect(url_for('home'))
    return render_template('createperson.html', form=person_form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)




