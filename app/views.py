from flask import render_template
from app import app

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