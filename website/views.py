from flask import Blueprint, render_template, request
import sqlite3
from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

conn = sqlite3.connect('baseDonnees.db', check_same_thread=False)
cur = conn.cursor()


@views.route('/boutique')
def boutique():
    liste = cur.execute("SELECT * FROM PRODUITS").fetchall()
    return render_template("boutique.html", tab= liste)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/<article>')
def article(article):
    liste = cur.execute("SELECT * FROM PRODUITS").fetchall()
    for el in liste:
        if article == el[2]:
            return render_template("article.html", el = el)

@views.route('/vendre',  methods=['GET','POST'])
def vendre():
    if request.method == "POST":
        path = request.form["path"]
        nom = request.form["name"]
        description = request.form["description"]
        prix = request.form["prix"]
        note = request.form["note"]
        #new_tab = [(str(path), str(nom), str(description), float(prix), float(note))]
        #cur.executemany("INSERT INTO PRODUITS(path, nom ,description, prix, note) VALUES(?, ?, ?, ?, ?)", new_tab)
        #conn.commit()

        file = request.form["fileordi"]
        filename = secure_filename(file)
        file.save('./static/images/', filename)

        return render_template("vendre.html")
    else:
        return render_template("vendre.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

