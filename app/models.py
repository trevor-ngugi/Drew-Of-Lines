from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog=db.relationship('Blog',backref='user',lazy='dynamic')
    comment=db.relationship('Comment',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__='blogs'
    id=db.Column(db.Integer,primary_key=True)
    author_id=db.Column(db.Integer,db.ForeignKey('users.id'))                                 
    blog_title=db.Column(db.String(255))
    blog_content=db.Column(db.String(255))#try using text
    blog_author=db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    

       
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    

    def __repr__(self):
        return f'Blog {self.blog_title}'

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id=db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,user_id):
        commentsretrieved = Comment.query.filter_by(user_id=user_id).all()#check whether it should be blog id
        return commentsretrieved

    def __repr__(self):
        return f'Comment {self.comment}'


class Role(db.Model):
    __tablename__= 'roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'



# class Comment:
#     all_comments=[]

#     def __init__(self,blog_id,blog,comment):#add blog_title
#         self.blog_id=blog_id
#         self.blog=blog
#         self.comment=comment

#     def save_comment(self):
#         Comment.all_comments.append(self)

#     @classmethod
#     def clear_reviews(cls):
#         Comment.all_comments.clear()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

