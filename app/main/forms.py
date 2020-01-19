from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required 

class CommentForm(FlaskForm):
    username=StringField('username',validators=[Required()])
    comment=TextAreaField('comment',validators=[Required()])
    submit=SubmitField('submit')