from flask import Flask, render_template, request, redirect, url_for, flash
from Forms import CreateUserForm, CreateCustomerForm
from flask_wtf.csrf import CSRFProtect
import shelve, User, Customer


app = Flask(__name__)  # Create the flask instance
csrf = CSRFProtect(app)
app.secret_key = 'jiceuiruineruiferuifbwneionweicbuivbruinewicwebvuierniwndiwebciuevbiuerdniweoncueivbuiecbwuicbewui'


@app.route('/')  # Creates a simple route, creates a connection between the URL / and a function that returns a
                 # response, the string 'Hello, World!'
def home():
    return render_template('home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.membership.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print("User ID:", user.get_user_id(), ", "
              "First Name:", user.get_first_name(), ", "
              "Last Name:", user.get_last_name(), ", "
              "Gender:", user.get_gender(), ", "
              "Remark:", user.get_remarks())

        db.close()

        flash("User successfully created!")
        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.gender.data, create_customer_form.membership.data,
                                     create_customer_form.remarks.data, create_customer_form.email.data,
                                     create_customer_form.date_joined.data,
                                     create_customer_form.address.data, )
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        # Test codes
        customers_dict = db['Customers']
        customer = customers_dict[customer.get_customer_id()]
        print("Customer ID:", customer.get_user_id(), ", "
              "First Name:", customer.get_first_name(), ", "
              "Last Name:", customer.get_last_name(), ", "
              "Gender:", customer.get_gender(), ", "
              "Membership:", customer.get_membership(), ", "
              "Remark:", customer.get_remarks(), ", "
              "Email:", customer.get_email(), ", "
              "Date Joined", customer.get_date_joined(), ", "
              "Address", customer.get_address())

        db.close()

        return redirect(url_for('home'))
    return render_template('createCustomer.html', form=create_customer_form)


if __name__ == '__main__':  # When a Python interpreter reads a Python file, it first sets a few special variables.
                            # Then it executes the code from the file. One of those variables is called __name__.

                            # When the interpreter runs a module, the __name__ variable will be set as  __main__
                            # if the module that is being run is the main program.
    app.run(port=5000, debug=True)

