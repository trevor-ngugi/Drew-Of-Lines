from . import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255))
    blog=db.relationship('Blog',backref='user',lazy='dynamic')
    

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

