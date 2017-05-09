import sys
import os
from flask import Flask, render_template, render_template_string, Markup, current_app, \
                  url_for
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from codecs import encode as codec_encode

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
PROJECT_DIR = 'projects'

app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_object(__name__)

# custom jinja functions

def url_for_tag(tag, rot13 = False):
    """
    Checks if icon for tag exists, if not, serve default icon url
    """
    icon_str= 'icons/{}.png'
    filepath = icon_str.format(tag.replace(' ', '_').lower())
    if os.path.isfile(os.path.join('static', filepath)):
        url = url_for('static', filename=filepath)
        return codec_encode(url, 'rot_13') if rot13 else url
    else:
        defpath = icon_str.format('default')
        url = url_for('static', filename=defpath)
        return codec_encode(url, 'rot_13') if rot13 else url

app.jinja_env.globals.update(url_for_tag=url_for_tag)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

@app.route("/")
def home():
    projects = get_projects()
    return render_template('home.html', projects=projects, current_page='Home')

@app.route("/projects/")
def projects():
    projects = get_projects()
    return render_template('projects.html',
                           projects=projects,
                           current_page='Projects')

@app.route('/projects/<name>/')
def project(name):
    path = '{}/{}'.format(PROJECT_DIR, name)
    print(path)
    project = flatpages.get_or_404(path)
    return render_template('project.html',
                           project=project,
                           current_page='Projects')

@app.route('/contact/')
def contact():
    return render_template('contact.html',
                           current_page='Contact')

def get_projects():
    projects = [p for p in flatpages if p.path.startswith(PROJECT_DIR)]
    projects.sort(key=lambda item:item['date'], reverse=False)
    return projects

if __name__ == "__main__":
    app.run(debug=True)
