from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(200))
    telephone = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    
    # Relaciones
    profile_develop = db.relationship("Developer", backref="user", uselist=False)
    profile_company = db.relationship("Company", backref="user", uselist=False)
    candidates = db.relationship("Candidate", backref="user", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "photo": self.photo,
            "telephone": self.telephone,
            "email": self.email,
            "country": self.country,
            "profile_develop": self.profile_develop.serialize() if self.profile_develop else None,
            "profile_company": self.profile_company.serialize() if self.profile_company else None,
            "candidates": [candidate.serialize() for candidate in self.candidates] if self.candidates else None
        }


    
class Developer(db.Model):
    __tablename__ = "developers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    
    # Clave foránea que referencia a User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relación con proyectos
    projects = db.relationship("Project", back_populates="developer", lazy=True)

    def __repr__(self):
        return f'<Developer {self.name} {self.last_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "description": self.description,
            "location": self.location,
            "projects": [project.serialize() for project in self.projects] if self.projects else None
        }


class Project(db.Model):
    __tablename__ = "projects"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    technologies = db.Column(db.String(140), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    
    # Clave foránea que referencia a Developer
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'), nullable=False)

    developer = db.relationship("Developer", back_populates="projects")

    def __repr__(self):
        return f'<Project {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "developer_id": self.developer_id
        }
    
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(200))
    telephone = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    
    profile_develop = db.relationship("Developer", backref="user", uselist=False)
    profile_company = db.relationship("Company", backref="user", uselist=False)
    candidates = db.relationship("Candidate", backref="user", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "photo": self.photo,
            "telephone": self.telephone,
            "email": self.email,
            "country": self.country,
            "profile_develop": self.profile_develop.serialize() if self.profile_develop else None,
            "profile_company": self.profile_company.serialize() if self.profile_company else None,
            "candidates": [candidate.serialize() for candidate in self.candidates] if self.candidates else None
        }


class Developer(db.Model):
    __tablename__ = "developers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(20), nullable=False)

    # Clave foránea que establece la relación con la tabla User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Developer {self.name} {self.last_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "description": self.description,
            "location": self.location,
            "user_id": self.user_id
        }


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    # Clave foránea que establece la relación con la tabla User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Company {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "user_id": self.user_id
        }


class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    resume = db.Column(db.String(200), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Candidate {self.name} {self.last_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "resume": self.resume,
            "user_id": self.user_id
        }

