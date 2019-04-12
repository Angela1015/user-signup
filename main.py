from flask import Flask, request, redirect 
import cgi
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')