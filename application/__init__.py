from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worktimeDB.db'
app.config['SECRET_KEY'] = 'pa55word!'

db = SQLAlchemy(app)


from application import routes