# Before using  SQLAlchemy(), import it from the flask_sqlalchemy module.
from flask_sqlalchemy import SQLAlchemy

# Initialize a `db` instance of the `SQLAlchemy` class`,
# Provide a connection to a database.
# The `db` object will be used to handle interactions with the database.
# It will manage the database connection,
# provide ORM functionality to map Python classes to database tables.
db = SQLAlchemy()


# Function to associate flask app with database variable
def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!


# Defines a class named Pet that inherits from db.Model. This tells Flask-SQLAlchemy that this class represents a database table.
# `db.Model` is a base class, a blueprint for creating database models.
# `Pet` class is a specific instance of that blueprint, tailored to represent pets in database.
class Pet(db.Model):

    # Assigns the name "pets" to the database table that will store information about our pets.
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), nullable=False, unique=True)

    species = db.Column(db.String(30), nullable=True)

    hunger = db.Column(db.Integer, nullable=False, default=20)

    # dunder
    # Better representation
    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"
