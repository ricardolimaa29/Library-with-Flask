from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length,Email
import datetime



app = Flask(__name__)
app.config["SECRET_KEY"] = "senha"


class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Senha",validators=[DataRequired(),Length(min=6)])
    submit = SubmitField("Entrar")


@app.route("/")
def index():
    date = datetime.datetime.now().strftime("%d-%m-%y")
    users = [ 
        {
        "name":"joao",
        "age":36,
        "email":"joao@gmail.com"
        },
        {
        "name":"Caio",
        "age":25,
        "email":"Caio@gmail.com"
        },
        {
        "name":"Ricardo",
        "age":24,
        "email":"Ricardo@gmail.com"
        },
        {
        "name":"Lucas",
        "age":30,
        "email":"Lucas@gmail.com"
        }
    ]
    return render_template(
        "index.html",
        users = users,
        date = date
    )

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)
