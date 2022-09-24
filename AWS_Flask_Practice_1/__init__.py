from flask import Flask, render_template


app = Flask(__name__)  # Create the flask instance


@app.route('/')  # Creates a simple route, creates a connection between the URL / and a function that returns a
                 # response, the string 'Hello, World!'
def home():
    return render_template('home.html')



@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


if __name__ == '__main__':  # When a Python interpreter reads a Python file, it first sets a few special variables.
                            # Then it executes the code from the file. One of those variables is called __name__.

                            # When the interpreter runs a module, the __name__ variable will be set as  __main__
                            # if the module that is being run is the main program.
    app.run()

