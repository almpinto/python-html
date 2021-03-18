from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'André'}
    posts = [
        {
            'author': {'username': 'Dr. Python'},
            'body': 'Não acaba essa Aula'
        },
        {
            'author': {'username': 'Eu'},
            'body': 'Não aguento mais'
        }
    ]
    return render_template('index.html', title='Estudando Flask Python', user=user, posts=posts)