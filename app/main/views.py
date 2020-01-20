from flask import render_template,redirect,url_for,abort,request
from . import main
from ..models import Comment,User,Blog
from .forms import CommentForm,UpdateProfile,BlogForm
from flask_login import login_required,current_user
from .. import db,photos
from datetime import datetime



#home page
@main.route("/")
def index():
    """
    views the index page and its data
    """
    title="Drew Of Lines"
    
    return render_template('index.html',title=title)

#writing a new blog
@main.route('/blog/new/',methods = ['GET','POST'])
@login_required
def new_blog():
    form=BlogForm()

    if form.validate_on_submit():
        blog_title=form.blog_title.data
        content=form.content.data
        author=form.author.data

        new_blog=Blog(id=id,blog_title=blog_title,blog_content=content,blog_author=author,author_id=current_user)
        new_blog.save_blog()
        # db.session.add(new_blog)
        # db.session.commit()
        return redirect(url_for('.index'))#error here

    title='read africa blog'
    return render_template('new_blog.html',title=title,blog_form=form)


# pathway to read more content
@main.route('/blog/<user_id>')
def blog(user_id):
    """
    views to show the authors blog
    """
    title="read blog"
    return render_template('blog.html',author=user_id,title=title)
    
#pathway to comment
@main.route('/blog/comment/<blog_id>',methods = ['GET','POST'],)
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


#pathway to profile page
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


#updating bio
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


#for updating the profile pic
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))