import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_object(__name__)

@app.route("/")
def home():
    posts = get_posts()
    return render_template('home.html', posts=posts)

@app.route("/posts/")
def posts():
    posts = get_posts()
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

def get_posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return posts

if __name__ == "__main__":
    app.run(debug=True)
