from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Default syntax in flask.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test01.db' # Create or connect to a database named test01.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Reduce memory usage.

db = SQLAlchemy(app) # Default syntax in SQLAlachemy.

# Use db.Table to create a table. subs means subscriptions. 
subs = db.Table("subs",
    db.Column("user_id", db.Integer, db.ForeignKey(user.user_id)),
    db.Column("channel_id", db.Integer, db.ForeignKey(channel.channel_id))
    )
# db.Table("Table_Name", db.Column("Column_Name", configs..., ForeignKey(Table_Name.Column_Name)), ...)

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

# The goal is connecting these two tablas. 
# I want to enable one user have many channels that belong to.
# And then one channel could have many users that are subscribed to that channel.
# To do that I need to create some kind of "Association Table."
# The Association Table will have two columns in it.
# One Column will be a user ID and the other column will be a channel ID.
# Every row represents a relationship between the two.

# The Association Table could be another model like User and Channel.
# But since I'm not really going to directly manipulate this table.
# It's better to create it just as a standalone table
# So it's not actually part of your model in a sense.
# But it is in the code and it's represented.
# I won't be able to directly modify it in my code.
# SQLAlchemy will handle updating this table.
# I'll just use db.Table to create a table.