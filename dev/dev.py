import requests


class DevTo(object):

    _URL = 'https://dev.to/api'

    def __init__(self, api_key):
        self._api_key = api_key
        
    def _get_url(self, path):
        return f'{self._URL}{path}'

    def _authentication(self):
        return {'api_key': self._api_key}

    def articles(self, id=None):
        '''
        This endpoint allows the client to retrieve a list of articles.
        "Articles" are all the posts that users create on DEV that typically
        show up in the feed. They can be a blog post, a discussion question,
        a help thread etc. but is referred to as article within the code.

        By default it will return featured, published articles ordered by descending popularity.

        Each page will contain 30 articles.

        Responses, according to the combination of params, are cached for 24 hours.

        learn more at:

        https://docs.dev.to/api/#operation/getArticles

        and

        https://docs.dev.to/api/#operation/getArticleById
        '''
        if id:
            articles = requests.get(url=self._get_url(path=f'/articles/{id}'))
        else:
            articles = requests.get(url=self._get_url(path=f'/articles/'))
        return articles.json()
