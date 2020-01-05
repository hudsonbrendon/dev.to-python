import requests


class DevTo(object):

    _URL = 'https://dev.to/api'

    def __init__(self, token):
        self._token = token

    def _get_url(self, path):
        return f'{self._URL}{path}'

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

        https://docs.dev.to/api/#tag/articles
        '''
        if id:
            request = requests.get(url=self._get_url(path=f'/articles/{id}'))
        else:
            request = requests.get(url=self._get_url(path=f'/articles/'))
        return request.json()
