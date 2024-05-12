# Currency Terminal

## Search
Details regarding the usage of the bonds search function.
```
https://bonds-terminal.vercel.app/search2/{query}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` | **Required**.|

```python
import requests

# Using the example query "apple".
url = "https://bonds-terminal.vercel.app/search2/apple"
response = requests.get(url)
data = response.json()

print(data)
# Will return Apple Bonds.
```
### Json Output Format:
```json
{
    "id": {
        "name": "string",
        "issuedate": "string",
        "maturitydate": "string",
        "issuer": "string",
        "isin": "string"
    },
```
## Fetch Bonds Details
Fetch specific bond information using 'id'.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**.|

```
https://bonds-terminal.vercel.app/search2/details/{id}
```
```python
import requests

# Using the example query "apple_incad-notes_201626-Bond-2026-au3cb0237881".
url = "https://bonds-terminal.vercel.app/search2/details/apple_incad-notes_201626-Bond-2026-au3cb0237881"
response = requests.get(url)
data = response.json()

print(data)
```
