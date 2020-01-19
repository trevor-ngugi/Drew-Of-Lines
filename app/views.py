from flask import render_template,redirect,url_for
from app import app
from .models import comments
from .forms import CommentForm
Comment=comments.Comment

#views
@app.route("/")
def index():
    """
    views the index page and its data
    """
    title="Drew Of Lines"
    return render_template('index.html',title=title)

@app.route('/blog/<user_id>')
def blog(user_id):
    """
    views to show the authors blog
    """
    title="read blog"
    return render_template('blog.html',author=user_id,title=title)
    

@app.route('/blog/comment/<blog_id>',methods = ['GET','POST'])
def new_comment(blog_id):
    form=CommentForm()

    if form.validate_on_submit():
        username=form.username.data
        comment=form.comment.data
        new_comment=Comment(blog_id,blog,comment)
        new_comment.save_comment()
        return redirect(url_for('blog',author = user_id ))

    title='read african blog'
    return render_template('comment.html',title=title,comment_form=form)