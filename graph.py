import requests
import plotly.express as px

from mdate import getdate

response=requests.get("https://www.bondsupermart.com/main/ws/v3/bond-info/bond-factsheet-chart/US594918BX11")
data=response.json()

print(data.keys())

ask=data["performanceChartMap"]["ONE_MTH"][0]["data"]
bid=data["performanceChartMap"]["ONE_MTH"][1]["data"]

print(ask)
print(bid)

askx=[]
asky=[]

bidx=[]
bidy=[]

for i in range(0,len(ask)):
    askx.append(getdate(ask[i][0]))
    asky.append(ask[i][1])
    bidx.append(getdate(bid[i][0]))
    bidy.append(bid[i][1])

fig = px.line(x=askx, y=asky, title='Graph')
fig.add_scatter(x=bidx,y=bidy)
fig.update_xaxes(
    title_text='Date',
    tickformat='%b %d, %Y',
    dtick=3 * 24 * 60 * 60 * 1000,  # Set the tick interval to one month
)


fig.show()
