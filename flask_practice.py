import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('hello.html')


@app.route("/welcome/<name>")
def welcome(name):
    return render_template('welcome.html', name=name)


def hello_world():
    return render_template('hello.html')


@app.route('/user')
def user_form():
    return render_template('user.html')


@app.route('/user-data', methods=['GET', 'POST'])
def user_data():
    if flask.request.method == 'POST':
        first_name = flask.request.form.get('fname')
        last_name = flask.request.form.get('lname')
        print(first_name, last_name)
        result = '''
            <h1> First Name: {} </h1>
            <h1> Last Name: {} </h1>
        '''
        return result.format(first_name, last_name)


if __name__ == '__main__':
    app.run()
