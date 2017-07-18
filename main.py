from app import *
from models import *
    
# TODO Rewrite to be home page    
@app.route('/', methods=['GET'])
def index():
    return redirect('/blog')

# TODO Rewrite to be all blog posts by all users
@app.route('/blog', methods=['POST', 'GET'])
def blog():
    posted_blog = Blog.query.all()
    return render_template('blog.html',title="My Blog!", 
        posted_blog=posted_blog)

@app.route('/selected_post', methods=['GET'])
def selected_post():
    blog_id = request.args.get('id')
    blog_post = Blog.query.filter_by(id=blog_id).first()
    return render_template('selectedpost.html', selected_post = blog_post)

@app.route('/newpost', methods=['POST', 'GET'])
def new_blog():
    if request.method == 'POST':
        #display errors for if no input in title or body
        blog_title = request.form['title']
        blog_body = request.form['body']
        new_blog = Blog(blog_title, blog_body)
        if not blog_title and not blog_body:
            flash ("Please type title and stuff in body")
            return render_template("newpost.html", title="New Post")
        if not blog_title:
            flash ("Please type a title")
            return render_template("newpost.html", title="New Post")
        if not blog_body:
            flash ("Please type stuff in body")
            return render_template("newpost.html", title="New Post")
        else:
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/blog')
    return render_template("newpost.html", title="New Post")

# TODO Create Login and Logout routes

if __name__ == '__main__':
    app.run()