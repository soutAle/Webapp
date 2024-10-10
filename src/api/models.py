from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(250), nullable=True)
    telephone = db.Column(db.String(30), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    country = db.Column(db.String(20), nullable=True)

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
            "is_active": self.is_active,
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
    projects = db.relationship("Project", backref="developer", lazy=True)

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

    def __repr__(self):
        return f'<Project {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "developer_id": self.developer_id
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

class Offer(db.Model):
    __tablename__ = "offers"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    contract_type = db.Column(db.String(50), nullable=False)

    # Clave foránea que referencia a Company
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

    def __repr__(self):
        return f'<Offer {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "salary": self.salary,
            "contract_type": self.contract_type,
            "company_id": self.company_id
        }

class Company(db.Model):
    __tablename__ = "companies"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(120), nullable=True)
    logo = db.Column(db.String(200), nullable=True)

    # Clave foránea que referencia a User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relación con la tabla 'offers'
    offers = db.relationship("Offer", backref="company", lazy=True)

    def __repr__(self):
        return f'<Company {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "website": self.website,
            "logo": self.logo,
            "user_id": self.user_id,
            "offers": [offer.serialize() for offer in self.offers] if self.offers else None
        }
    

class bookmark(db.Model):
    __tablename__ = "bookmarks"
    id = db.Column(db.Integer, primary_key=True)

    # Claves foraneas que representan aa Developer, Company y Offer
    developer_id = db.Column(db.Integer, db.ForeignKey("developers.id"), nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=True)
    offer_id = db.Column(db.Integer, db.ForeignKey("offers.id"), nullable=True)

    def __repr__(self):
        return f'<Favoritos {self.developer_id}-{self.company_id}-{self.offer_id}>'

    def serialize(self):
        return {
            "developer_id": self.programador_id,
            "company_id": self.company_id,
            "offer_id": self.offer_id
        }
    
    