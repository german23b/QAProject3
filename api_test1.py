#- Check that the url for fail isn’t : “https:google.com
import requests

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/fail'
response = requests.get(url)
response.url
if response.url != 'https://www.google.com':
    print('success')
else:
    print('failed')



