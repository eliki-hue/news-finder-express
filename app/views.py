
from flask import render_template
from app import app
from app.requests import get_channels



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