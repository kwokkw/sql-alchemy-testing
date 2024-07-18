from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from testing_models import db, connect_db, Pet

app = Flask(__name__)

""" CONFIGURATION BEFORE CONNECTING TO DATABASE """

# Telling Flask-SQLAlchemy to use PostgreSQL as the database for the application and to connect to a database named `pet_shop_db`
# Where is the database?
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgres://postgres:Kwok17273185@localhost:5432/pet_shop_db"
)
# By default, Flask-SQLAlchemy tracks modifications to objects in a session and signals the application whenever there are changes.
# Setting `SQLALCHEMY_TRACK_MODIFICATIONS` to False disables tracking behavior, potentially improving performance.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Determines whether SQLAlchemy should print out all SQL statements it executes.
# Print all SQL statements to the terminal (helpful for debugging)
app.config["SQLALCHEMY_ECHO"] = True

# By setting the `SECRET_KEY`, enable Flask to use it for securing cookies, sessions, and potentially other security mechanisms within your application. MORE TO COME...
app.config["SECRET_KEY"] = "chickenzarecool21837"

# Debug toolbar is configured to NOT intercept redirects,
# allowing redirects to proceed normally
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# Initializes and integrates the Flask Debug Toolbar into the Flask application (`app`), providing debugging capabilities during development.
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template("list.html", pets=pets)
