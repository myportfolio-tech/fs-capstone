from staffer import db
from datetime import datetime
from sqlalchemy.orm import relationship



class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(60), nullable=False)
    
    def __rep__(self):
        return f"User('{self.username}' , '{self.email}')"

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()




class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.SmallInteger, unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    advisor_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    
    advisor = relationship("Employee", foreign_keys=[advisor_id])
    manager = relationship("Employee", foreign_keys=[manager_id])
    director = relationship("Employee", foreign_keys=[director_id])
    
    def __rep__(self):
        return f"User('{self.username}' , '{self.email}')"

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
