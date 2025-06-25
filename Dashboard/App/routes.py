from flask import render_template, redirect, url_for
from App.form import Form
from App import app
from App import sqlite

@app.route('/')
@app.route('/index')
def index():
    posts = sqlite.get_data()
    form = Form()
    return render_template('index.html', form=form, posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def handle_form():
    form = Form()
    if form.validate_on_submit():
        sqlite.insert_into(form.username.data, form.comment.data)
        return redirect(url_for('index'))
    posts = sqlite.get_data()
    return render_template('index.html', form=form, posts=posts)