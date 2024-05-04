from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
user = "Max"


@app.route("/")
def courses():
    return render_template("courses.html", user=user)


@app.route("/cours_1")
def cours_1():
    text_1 = 1
    text_2 = 2
    text_3 = 3
    return render_template("cours_1.html", text_1=text_1, text_2=text_2, text_3=text_3, user=user)


@app.route("/cours_2")
def cours_2():
    text_1 = 4
    text_2 = 5
    text_3 = 6
    return render_template("cours_2.html", text_1=text_1, text_2=text_2, text_3=text_3, user=user)


@app.route("/cours_3")
def cours_3():
    text_1 = 7
    text_2 = 8
    text_3 = 9
    return render_template("cours_3.html", text_1=text_1, text_2=text_2, text_3=text_3, user=user)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        return redirect(url_for('layout'))
    return render_template('registration.html')


@app.route('/admin_panel')
def admin_panel():
    return render_template('admin_panel.html')


@app.route('/layout')
def layout():
    return render_template('layout.html', user=user)


@app.route('/tests')
def test():
    return render_template('tests.html')


if __name__ == "__main__":
    app.run(debug=True)
