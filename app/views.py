
from flask import render_template
from app import app
from app.models import channel
from app.requests import get_channels,process_result



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # getting channels
    channels = get_channels('sources')
    print(channels)
    
    title = 'Welcome to this website that displays all the news channels'
    return render_template('index.html', title =title, sources= channels)

@app.route('/news/<name>')
def get_channel(name):
    '''function that goes to the home page of selected news source'''
    