from DBConnect import app
from flask import Flask, render_template


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/find2/')
def find():
    return render_template('find.html')


@app.route('/register/')
def register():
    return render_template('registration.html')


@app.route('/delete/')
def delete():
    return render_template('delete.html')


@app.route('/update/')
def update():
    return render_template('update.html')

