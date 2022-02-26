class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'

    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'

    # ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    




class ProdConfig(Config):
    '''Production  configuration child class'''

    pass


class DevConfig(Config):
    '''Development  configuration child class'''

    DEBUG = True