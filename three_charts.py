# three_charts.py

#
# CHART 1 (PIE)
#
import plotly
import plotly.graph_objects as go
#plotly.graph_objects

#plotly.offline.plot({
#    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#    "layout": go.Layout(title="hello world")
#}, auto_open=True)
#
pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

labels = [p["company"] for p in pie_data]
values = [p["market_share"] for p in pie_data]

trace = go.Pie(labels=labels, values=values)

#plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)



print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

#
# CHART 2 (LINE)
#
line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

plotly.offline.plot({
    "data": [go.Scatter(x=[line["date"] for line in line_data], y=[line["stock_price_usd"] for line in line_data])],
    "layout": go.Layout(title="hello world")
}, auto_open=True)


line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]


fig = go.Figure(go.Bar(
            x=[data["genre"] for data in bar_data],
            y=[data["viewers"] for data in bar_data],
            orientation='v'))

fig.show()
print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data