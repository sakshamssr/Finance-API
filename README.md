# Finance Api

## Search Bonds
Details regarding the usage of the bonds search function.
```
https://finance-api-ssr.vercel.app/search2/{query}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` | **Required**.|

```python
import requests

# Using the example query "apple".
url = "https://finance-api-ssr.vercel.app/search2/apple"
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
https://finance-api-ssr.vercel.app/search2/details/{id}
```
```python
import requests

# Using the example query "apple_incad-notes_201626-Bond-2026-au3cb0237881".
url = "https://finance-api-ssr.vercel.app/search2/details/apple_incad-notes_201626-Bond-2026-au3cb0237881"
response = requests.get(url)
data = response.json()

print(data)
```
### Json Output Format:
```json
{
    "ISIN": "AU3CB0237881",
    "Name": "APPLE  2026",
    "Country": "USA",
    "Issuer": "Apple Inc.",
    "Issue Volume": "325,000,000",
    "Currency": "AUD",
    "Issue Price": "99.92",
    "Issue Date": "6/10/2016",
    "Coupon": "3.600%",
    "Denomination": "10000",
    "Quotation Type": "",
    "Payment Type": "regular interest",
    "Special Coupon Type": "",
    "Maturity Date": "6/10/2026",
    "Coupon Payment Date": "6/10/2024",
    "Payment Frequency": "",
    "No. of Payments per Year": "2.0",
    "Coupon Start Date": "12/10/2016",
    "Final Coupon Date": "6/9/2026",
    "Floater?": "No",
    "rating": 99,
    "color": "green",
    "graphdata": "string"
}
```

