import sys
import os
import datetime
import json
import math
from flask import Flask, render_template, render_template_string,\
                  Markup, current_app, \
                  url_for, redirect
from flask_flatpages import FlatPages, pygments_style_defs
from flask_flatpages.utils import pygmented_markdown


cfd = os.path.dirname(os.path.realpath(__file__))
POST_DIR = 'posts'
PROJECT_DIR = 'projects'
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
    return pygments_style_defs('vs'), 200, {'Content-Type': 'text/css'}

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

@app.route("/")
def home():
    posts, _ = get_items(POST_DIR, 6, pinned_only=True)
    projects, _ = get_items(PROJECT_DIR, 4, pinned_only=True)

    return render_template('home.html',
                           posts=posts,
                           projects=projects,
                           current_page='Home')

@app.route("/me/")
def me():
    return redirect(url_for("about"))


@app.route("/posts/", defaults={'pagenum': 1})
@app.route("/posts/page/<pagenum>/")
def posts(pagenum):
    items, maxpages = get_items(POST_DIR, 12, page=int(pagenum))
    return render_template('posts.html',
                            posts=items,
                            current_page='Posts',
                            pagenum=int(pagenum),
                            maxpages=maxpages)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    item = flatpages.get_or_404(path)
    return render_template('post.html',
                            post=item,
                            current_page='Posts')


@app.route("/projects/", defaults={'pagenum': 1})
@app.route("/projects/page/<pagenum>/")
def projects(pagenum):
    items, maxpages = get_items(PROJECT_DIR, 8, page=int(pagenum))
    items.sort(key=lambda x: x['pin_rank'], reverse=True)
    return render_template('projects.html',
                            projects=items,
                            current_page='Projects',
                            pagenum=int(pagenum),
                            maxpages=maxpages)


@app.route('/projects/<name>/')
def project(name):
    path = '{}/{}'.format(PROJECT_DIR, name)
    item = flatpages.get_or_404(path)
    return render_template('project.html',
                            project=item,
                            current_page='Projects')

@app.route('/about/')
def about():
    return render_template('about.html',
                           current_page='About')

@app.route('/contact/')
def contact():
    return render_template('contact.html',
                           current_page='Contact')

@app.route('/publications/')
def publications():
    pub = flatpages.get_or_404("publications")
    return render_template('publications.html',
                           current_page='Publications',
                           publications_page=pub)

@app.route('/static/')
def st():
    return ""

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='me_circ.png')

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


def get_items(pattern, limit, pinned_only=False, page=1):
    items = [p for p in flatpages if p.path.startswith(pattern)]
    if pinned_only:
        items = [p for p in items if 'pin_rank' in p.meta]
        items.sort(key=lambda x: x['pin_rank'], reverse=True)
    else:
        items.sort(key=lambda item: item['date'], reverse=True)
    first = (page - 1) * limit
    last = first + limit
    maxpages = math.ceil(len(items) / limit)
    items = items[first:last]
    return items, maxpages

if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.10')
