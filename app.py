from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:SaiPrasanth@localhost:5432/aadhya'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key in a real applicationdb = SQLAlchemy(app)

db = SQLAlchemy(app)


# Database Models
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable= False)
    content = db.Column(db.Text, nullable=False)





# Resource Classes for API functionality
class BlogPostResource(Resource):
    def get(self):
        posts = BlogPost.query.all()
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])






# API End Points
api.add_resource(BlogPostResource, "/blog")





#  Create Database Tables while initial Run
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()
    app.run(debug = True)