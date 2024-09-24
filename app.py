from flask import Flask
# from app.routes import app, db
from application import app

if __name__ == "__main__":
    app.run(debug = True)