import pytest
import requests


class TestApi:
    def test_1(self):
        import requests

        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/fail'
        response = requests.get(url)
        response.url
        if response.url != 'https://www.google.com':
            print('success')
        else:
            print('failed')

    def test_2(self):
        import requests

        url = 'https://creativecommons.org/licenses/by-sa/3.0'
        response = requests.get(url)
        flag = False
        if 400 > response.status_code >= 200:
            flag = True
        assert flag == True
