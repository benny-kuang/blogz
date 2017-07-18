from app import db

# stores all the blog posts
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    # owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, title, body): # add owner
        self.title = title
        self.body = body
        # self.owner = owner

# stores all users
'''class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    posts = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password'''