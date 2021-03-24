from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://project1:project1@localhost/project1"
db = SQLAlchemy(app)
migrate=Migrate(app,db) #Initializing migrate.
manager = Manager(app)
manager.add_command('db',MigrateCommand)

class property(db.Model):
    title= db.column(db.String)
    description= db.Column(db.String(255)) 
    noofrooms= db.column(db.integer)
    noofbathrooms =db.column(db.Integer)
    price= db.column(db.float)
    propertytype= db.column(db.string)
    location=db.column(db.String) 
    photo=db.column()
    propertyid= db.column(db.Integer, primary_key=True, unique=True)


if __name__ == "__main__":
     manager.run()