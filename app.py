# from flask import Flask
from application.routes import app
# from application import app

if __name__ == "__main__":
    app.run(debug = True)