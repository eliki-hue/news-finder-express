from app import app
import urllib.request, json
from models import channel

Channel = channel.Channel


# Getting api key
api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_channels(search):
    '''
    function that gets the json responce to the channel source request
    '''
    get_news_url = base_url.format(search,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_result = None

        news_result = process(get_news_response)
        return news_result
        

def process(channel):
    '''
    function that processes channel results
    '''
    channel_info = []
    for item in channel:
        id = channel.get('id')
        name = channel.get('name')
        description = channel.get('description')
        url = channel.get('url')
        category = channel.get('category')
        country = channel.get('country')

        channel_object = Channel(id, name, description, url, category, country)
        channel_info.append(channel_object)

    return channel_info
    

