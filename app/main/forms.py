from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required 

class BlogForm(FlaskForm):
    blog_title=StringField('blog title',validators=[Required()])
    content=TextAreaField('comment',validators=[Required()])
    author=TextAreaField('author',validators=[Required()])
    submit=SubmitField('submit')


class CommentForm(FlaskForm):
    username=StringField('username',validators=[Required()])#can remove this
    comment=TextAreaField('comment',validators=[Required()])
    submit=SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')