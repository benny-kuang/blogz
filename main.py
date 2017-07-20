from app import *
from models import *
'''Restrict and redirect user to signup or login if trying to post w/o being logged in
Require login'''
# # TODO Require login
@app.before_request
def require_login():
    allowed_routes = ['index', 'blog', 'signup', 'login']
    if request.endpoint not in allowed_routes and 'user' not in session:
        return redirect('/login')

# Homepage displays all users. Clicking User will redirect to posts made by that user
@app.route('/', methods=['GET'])
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

'''
# # TODO Rewrite to be all blog posts by all users
# # Displays all blogs in database, or just specific post if an ID is passed as GET
# @app.route('/blog', methods=['POST', 'GET'])
# def blog_postings():

This is similar to what is above
@app.route('/selected_post', methods=['GET'])
def selected_post():
    blog_id = request.args.get('id')
    blog_post = Blog.query.filter_by(id=blog_id).first()
    return render_template('selectedpost.html', selected_post = selected_post)
'''

# # TODO Display all blog posts written by specific user
# @app.route('/singleuser')
# def singleuser():

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']

# Error prompts
        error = validate(username, password, verify)
        if error[0] or error[1] or error[2]:
            if error[0] != "":
                flash(error[0], 'error')
            if error[1] != "":
                flash(error[1], 'error')
            if error[2] != "":
                flash(error[2], 'error')
            return render_template("signup.html", username=username)
        #if no errors and user is not already in database, new user added to db and logged in
        else:
            user = User.query.filter_by(username=username).first()
            if not user:
                new_user = User(username, password)
                db.session.add(new_user)
                db.session.commit()
                session['user'] = new_user.username
                return redirect('/signup')
            else:
                flash('Username already in use', 'error')
    return render_template('signup.html')
        
# TODO Create Login and Logout routes
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and password:
            session['user'] = user.username
            flash("Logged in", "success")
            return redirect('/login')
        else:
            flash('Username or Password Incorrect', 'error')
    return render_template('login.html')

# # TODO Create logout routes
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'user' in session:
        del session['user']
    return redirect('/login')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        #display errors for if no input in title or body
        owner = User.query.filter_by(username=session['user']).first()
        post_title = request.form['title']
        post_body = request.form['body']
        new_post = Blog(post_title, post_body, owner)
        if not post_title and not post_body:
            flash ("Please type title and stuff in body")
            return render_template("newpost.html", title="New Post")
        if not post_title:
            flash ("Please type a title")
            return render_template("newpost.html", title="New Post")
        if not post_body:
            flash ("Please type stuff in body")
            return render_template("newpost.html", title="New Post")
        else:
            db.session.add(new_post)
            db.session.commit()
            # TODO: Redirect to page with newly posted individual blog
            return redirect('/blog')
    return render_template("newpost.html", title="New Post")

if __name__ == '__main__':
    app.run()