
from flask import render_template
from app import app
from app.models import channel
from app.requests import get_channels,get_source_articles




# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # getting channels
    channels = get_channels('sources')
    print(channels)
    
  
    return render_template('index.html', sources= channels)

@app.route('/news/<id>')
def articles(id):
    '''
    article view to display all article from a given source
    '''
    visited = get_source_articles(id)
    title = id 
    return render_template('articles.html', title=title, articles=visited)