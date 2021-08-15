from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Default syntax in flask.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test01.db' # Create or connect to a database named test01.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Reduce memory usage.

db = SQLAlchemy(app) # Default syntax in SQLAlachemy.

# Create a table named User. db.Model is default syntax in flask_sqlalchemy.
class User(db.Model):
    __tablename__ = "user" # It's ok not to  code is line.
    # When we class User, system will automatically lowercase User as the name.
    # Unless you want to change the name of the table on purpose.
    user_id = db.Column(db.Integer, primary_key=True) # The first column is user_id. It's a Integer and primary key.
    name = db.Column(db.String(20)) # The second column is name. It's a string up to 20 characters.

# Create a table named Channel.
class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(30))
