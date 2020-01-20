from flask import render_template,redirect,url_for,abort
from . import main
from ..models import Comment,User
from .forms import CommentForm
from flask_login import login_required


#views
@main.route("/")
def index():
    """
    views the index page and its data
    """
    title="Drew Of Lines"
    return render_template('index.html',title=title)

@main.route('/blog/<user_id>')
def blog(user_id):
    """
    views to show the authors blog
    """
    title="read blog"
    return render_template('blog.html',author=user_id,title=title)
    

@main.route('/blog/comment/<blog_id>',methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form=CommentForm()

    if form.validate_on_submit():
        username=form.username.data
        comment=form.comment.data
        new_comment=Comment(blog_id,blog,comment)
        new_comment.save_comment()
        return redirect(url_for('.blog',author = user_id ))

    title='read african blog'
    return render_template('comment.html',title=title,comment_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)