#Check that the url for fail is : “https://creativecommons.org/licenses/by-sa/3.0"

import requests

url = 'https://creativecommons.org/licenses/by-sa/3.0'
response = requests.get(url)

if 400 > response.status_code >= 200:
    print('success')
else:
    print('failed')
