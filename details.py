import requests

# Using the example query "python".
url = "https://gnewssapi.vercel.app/news/finance"
response = requests.get(url)
data = response.json()

print(data["0"]["title"])
