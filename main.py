import flask
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from notification_manager import NotificationManager
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'rusyasuper_likes_babyes'
# ckeditor = CKEditor(app)
Bootstrap(app)

#CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arina_baza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#CONFIGURE TABLE
class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    number = db.Column(db.Text, unique=True, nullable=False)
    date = db.Column(db.Text, nullable=False)
    type_of_service = db.Column(db.Text)


##WTForm

# db.create_all()


@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/about_me")
def about():
    return render_template("about.html")


@app.route("/prices")
def contact():
    return render_template("price.html")


@app.route("/gallery")
def new_post():
    return render_template("gallery.html")


@app.route("/gallery2")
def me():
    return render_template("gallery2.html")

@app.route("/action_page1", methods=['POST'])
def send_sms():
    name = request.form['name']
    number = request.form['number']
    text = request.form['opisanie']
    dicton = {
        'Имя': name,
        'Номер': number,
        'Описание': text,
        'Тип': 'Одиночная съемка',
    }
    flaers = db.session.query(Buyer).filter((Buyer.number == number))
    if not flaers:
        now = datetime.datetime.today()
        nowwow = now.strftime('%m/%d/%y')
        buyer = Buyer(name=name, number=number, date=nowwow, type_of_service='Одиночная')
        db.session.add(buyer)
        db.session.commit()
    else:
        flash("Спасибо, что вернулись к нам! Мы очень рады постоянным клиентам:)", 'success')
    sms = NotificationManager()
    sms.getsalut(dicton)
    return redirect('/')


@app.route("/action_page2", methods=['POST'])
def send_sms2():
    name = request.form['name']
    number = request.form['number']
    text = request.form['opisanie']
    dicton = {
        'Имя': name,
        'Номер': number,
        'Описание': text,
        'Тип': 'Съемка мероприятий',
    }
    flaers = db.session.query(Buyer).filter((Buyer.number == number))
    if not flaers:
        now = datetime.datetime.today()
        nowwow = now.strftime('%m/%d/%y')
        buyer = Buyer(name=name, number=number, date=nowwow, type_of_service='Мероприятия')
        db.session.add(buyer)
        db.session.commit()
    else:
        flash("Спасибо, что вернулись к нам! Мы очень рады постоянным клиентам:)", 'success')
    sms = NotificationManager()
    sms.getsalut(dicton)
    return redirect('/')


@app.route("/action_page3", methods=['POST'])
def send_sms3():
    name = request.form['name']
    number = request.form['number']
    text = request.form['opisanie']
    dicton = {
        'Имя': name,
        'Номер': number,
        'Описание': text,
        'Тип': 'Прочее',
    }
    flaers = db.session.query(Buyer).filter((Buyer.number == number))
    if not flaers:
        now = datetime.datetime.today()
        nowwow = now.strftime('%m/%d/%y')
        buyer = Buyer(name=name, number=number, date=nowwow, type_of_service='Прочее')
        db.session.add(buyer)
        db.session.commit()
    else:
        flash("Спасибо, что вернулись к нам! Мы очень рады постоянным клиентам:)", 'success')
    sms = NotificationManager()
    sms.getsalut(dicton)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=False)
