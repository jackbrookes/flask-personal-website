import sys
import os
import datetime
import json
import math
from flask import Flask, render_template, render_template_string,\
                  Markup, current_app, \
                  url_for
from flask_flatpages import FlatPages, pygments_style_defs
from flask_flatpages.utils import pygmented_markdown

cfd = os.path.dirname(os.path.realpath(__file__))
POST_DIR = 'posts'
app = Flask(__name__)
app.config.from_pyfile('config.py')
flatpages = FlatPages(app)

with open(os.path.join(cfd, 'tagmap.json')) as json_data:
    tag_map = json.load(json_data)

# custom jinja functions
@app.context_processor
def utility_processor():

    def url_for_tag(tag):
        icon_str= 'icons/{}.png'
        filepath = icon_str.format(tag.replace(' ', '_').lower())
        if os.path.isfile(os.path.join('static', filepath)):
            url = url_for('static', filename = filepath)
            return url
        else:
            defpath = icon_str.format('default')
            url = url_for('static', filename = defpath)
            return url

    year = datetime.datetime.now().strftime('%Y')

    def get_tag_property(tagname, property):
        if tagname in tag_map:
            if property in tag_map[tagname]:
                return tag_map[tagname][property]
            else:
                return ""
        else:
            if property in tag_map['default']:
                return tag_map['default'][property]
            else:
                return ""

    return dict(url_for_tag = url_for_tag,
                year = year,
                get_tag_property = get_tag_property)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('friendly'), 200, {'Content-Type': 'text/css'}

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

@app.route("/")
def home():
    posts, _ = get_posts(4, pinned_only = True)
    return render_template('home.html',
                           posts = posts,
                           current_page='Home')

@app.route("/me/")
def me():
    return render_template('me.html')

@app.route("/posts/", defaults={'pagenum': 1})
@app.route("/posts/page/<pagenum>/")
def posts(pagenum):
    posts, maxpages = get_posts(8, page = int(pagenum))

    return render_template('posts.html',
                           posts=posts,
                           current_page='Posts',
                           pagenum = int(pagenum),
                           maxpages = maxpages)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html',
                           post=post,
                           current_page='Posts')

@app.route('/about/')
def about():
    return render_template('about.html',
                           current_page='About')

@app.route('/contact/')
def contact():
    return render_template('contact.html',
                           current_page='Contact')

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='me_circ.png')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def get_posts(limit, pinned_only = False, page = 1):
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    if pinned_only:
        posts = [p for p in posts if 'pin_rank' in p.meta]
        posts.sort(key=lambda item:item['pin_rank'], reverse=True)
    else:
        posts.sort(key=lambda item:item['date'], reverse=True)
    first = (page - 1) * limit
    last = first + limit
    maxpages = math.ceil(len(posts) / limit)
    posts = posts[first:last]
    return posts, maxpages

if __name__ == "__main__":
    app.run(debug = True)
