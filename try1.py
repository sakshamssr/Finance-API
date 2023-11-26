import requests

# URL of the website
url = 'https://markets.businessinsider.com/bonds/apple_incad-notes_201626-bond-2026-au3cb0237881?miRedirects=1'

# Make a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Find API links in the XHR requests
    for entry in response.history + [response]:
        referer_header = entry.request.headers.get('referer')
        if referer_header:
            print('Found XHR request, Referer:', referer_header)
            print('Request URL:', entry.url)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
