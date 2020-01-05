class DevTo(object):

    _URL = 'https://dev.to/api'

    def __init__(self, token):
        self._token = token

    def _get_url(self, path):
        return f'{self._URL}{path}'
