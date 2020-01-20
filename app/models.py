from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog=db.relationship('Blog',backref='user',lazy='dynamic')

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
    blog_title=db.Column(db.String(255))
    blog_content=db.Column(db.String(255))#try using text
    blog_author=db.Column(db.String(50))
    author_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    
    #postedat

    def __repr__(self):
        return f'Blog {self.blog_title}'



class Comment:
    all_comments=[]

    def __init__(self,blog_id,blog,comment):#add blog_title
        self.blog_id=blog_id
        self.blog=blog
        self.comment=comment

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_reviews(cls):
        Comment.all_comments.clear()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

