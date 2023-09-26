from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if name == '':
            raise ValueError('Need a name')
        return name

    @validates('phone_number')
    def validate_number(self, key, number):
        if len(number) != 10:
            raise ValueError('Need 10 digits for a number')
        return number


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String,)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())



    @validates('content')
    def validate_content(self, key, content):
        if len(content) <= 250:
            raise ValueError('Content is too short')
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError('Content is too long')
        return summary

    @validates('category')
    def validate_category(self, key, category):
        excepeted_categories=['Fiction', 'Non-Fiction']
        if category not in excepeted_categories:
            raise ValueError('Incorrect Category')
        return category

    @validates('title')
    def validate_bait(self, key, title):
        excepeted_titles=["Won't Believe", "Secret","Top", "Guess"]
        if title not in excepeted_titles:
            raise ValueError('Invalid Click Bait Title')
        elif title == '':
            raise ValueError("No title")
        return title

    

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
