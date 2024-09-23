from application import app, db
from flask import render_template, redirect, flash, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import WorkTime




@app.route("/")
def index(): 
    return render_template('index.html', title = 'home')

@app.route("/add", methods = [ "GET", "POST"])
def add():
    form = UserInputForm()
    if form.validate_on_submit():
        new_entry = WorkTime(
            id=form.id.data,
            name=form.name.data,
            time_in=form.time_in.data,
            time_out=form.time_out.data,
            month=form.month.data,
            date=form.date.data,
            workday_type=form.workday_type.data
        )
        db.session.add(new_entry)
        db.session.commit()
        flash(f"{form.workday_type.data} has been added successfully", "success")
        return redirect(url_for('index'))
    return render_template('add.html', title='add hours', form=form)

@app.route("/dashboard")
def dashboard(): 
    return render_template('dashboard.html', title = 'dashboard')

@app.route("/layout")
def layout(): 
    return render_template('layout.html', title = 'layout')