from app import *
from hashutils import *
from datetime import datetime

# stores all the blog posts
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    pub_date = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))



    def __init__(self, title, body, owner, pub_date=None):
        self.title = title
        self.body = body
        self.owner = owner
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

# stores all users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(600))
    posts = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)

# used for signup verification
def validate(username, password, verify):
    error = {0: '', 1:'', 2:''}

    if len(username) < 3 or len(username) > 20:
        error[0] = "Username must be within 3 and 20 characters."
    
    elif re.search(r'\s', username):
        error[0] = "Please no spaces in username"

    if len(password) < 3 or len(password) > 20:
        error[1] = "Password must be within 3 and 20 characters"

    elif re.search(r'\s', password):
        error[1] = "Please no spaces in password"

    if verify == "":
        error[2] = "Please re-enter password"

    elif verify != password:
        error[2] = "Password does not match.  Please re-enter."

    return error