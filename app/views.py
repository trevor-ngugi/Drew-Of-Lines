from flask import render_template
from app import app

#views
@app.route("/")
def index():
    """
    views the index page and its data
    """
    return render_template('index.html')

@app.route('/blog/<user_id>')
def blog(user_id):
    """
    views to show the authors blog
    """
    return render_template('blog.html',author=user_id)