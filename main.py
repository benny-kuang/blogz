from app import *
from models import *
from hashutils import *

# Loads user into a session
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

# This redirects anonymous to login when they try to go to the New Post page
@login_manager.unauthorized_handler
def unauthorized():
    flash('Please login in order to post', 'error' )
    return redirect('/login')

# The homepage displays all the users
@app.route('/', methods=['GET'])
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


# TODO Include pagination and dating of posts
# Displays all blogs in database, or just specific post if an ID is passed as GET
@app.route('/blog', methods=['POST', 'GET'])
def blog_postings():
    
    # if query is id or user (blog?id=) or (blog?user=)
    post_id = request.args.get('id')
    user_id = request.args.get('user')
    # This selects individual post
    if post_id:
        posts = Blog.query.filter_by(id=[post_id]).all()
        return render_template("blog.html", posts=posts)
    # This selects all posts by a given user
    if user_id:
        posts = Blog.query.filter_by(owner_id = user_id).order_by(Blog.pub_date.desc()).all()
        return render_template("singleUser.html", posts=posts)
    # Default view: All blog posts by all users
    posts = Blog.query.order_by(Blog.pub_date.desc()).all()
    return render_template("blog.html", posts=posts)

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
                login_user(new_user)
                flash('User successfully registered', 'success')
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
        if user and check_pw_hash(password, user.pw_hash):
            login_user(user)
            flash("Logged in", 'success')
            return redirect(url_for('new_post'))
        else:
            flash('Username or Password Incorrect', 'error')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Logged out", "success")
    return redirect('/login')

@app.route('/newpost', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        #display errors for if no input in title or body
        owner = User.query.filter_by(id=current_user.id).first()
        post_title = request.form['title']
        post_body = request.form['body']
        new_post = Blog(post_title, post_body, owner)
        if not post_title and not post_body:
            flash ("Please type title and stuff in body", 'error')
            return render_template("newpost.html", title="New Post")
        if not post_title:
            flash ("Please type a title", 'error')
            return render_template("newpost.html", title="New Post")
        if not post_body:
            flash ("Please type stuff in body", 'error')
            return render_template("newpost.html", title="New Post")
        else:
            db.session.add(new_post)
            db.session.commit()
            # TODO: Redirect to page with newly posted individual blog
            return redirect('/blog')
    return render_template("newpost.html", title="New Post")

if __name__ == '__main__':
    app.run()