from app import app
import urllib.request, json
from .models import channel

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
        news_results =None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_result(news_results_list)



        
        return news_results
        

def process_result(news_lists):
    
    '''
    function that processes channel results
    '''
   
    channel_info = []
    
        
    # channel_info.append(news_lists)

            # id = news_list[0]
            # name = news_list[1]
            # description = news_list[2]
            # url = news_list[3]
            # category = news_list[4]
            # country = news_list[5]

            # channel_object = Channel(id, name, description, url, category, country)
            # channel_info.append(channel_object)
           
    return news_lists


