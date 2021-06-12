# import plotly.graph_objects as go

# import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
# df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

# fig = go.Figure(data=go.Scattergeo(
#         lon = df['long'],
#         lat = df['lat'],
#         text = df['text'],
#         mode = 'markers',
#         marker_color = df['cnt'],
#         ))

# fig.update_layout(
#         title = 'Most trafficked US airports<br>(Hover for airport names)',
#         geo_scope='usa',
#     )
# fig.show()
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

data = pd.read_csv("truck1.csv")
data = data.ffill().bfill()
print(data.shape)
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
#                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                   mapbox_style="carto-positron")

# us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
# us_cities = us_cities.query("State in ['New York', 'Ohio']")

# fig = px.line_mapbox(us_cities, lat="lat", lon="lon", color="State", zoom=3, height=300)

# fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,
#     margin={"r":0,"t":0,"l":0,"b":0})

fig = px.line_mapbox(lat=data['Latitude'], lon=data['Longitude'],
                     mapbox_style = 'open-street-map',zoom=7)


# fig = go.Figure(go.Scattermapbox(
#     mode = "markers+lines",
#     lon = data['Latitude'][:3],
#     lat = data['Longitude'][:3],
#     marker = {'size': 10}))

# fig.add_trace(go.Scattermapbox(
#     marker = {'size':2}))

# fig.update_layout(
#     margin ={'l':0,'t':0,'b':0,'r':0},
#     mapbox = {
#         'center': {'lon': 18, 'lat': 73},
#         'style': "stamen-terrain",
#         'center': {'lon': 19, 'lat': 74},
#         'zoom': 1})


app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])




if __name__ == "__main__":
    app.run_server(debug=True)





import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import plotly.express as px

data = pd.read_csv("truck1.csv")
# data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")
# data['date_only'] = data["Date"].dt.date

print("working..")

data = data.ffill().bfill()
# data.sort_values("Date", inplace=True)
# app = dash.Dash(__name__)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Automobile Analytics"

name=['Date','Latitude', 'Longitude', 'Altitude', 'RPM',
        'Driver Demand Torque (%)', 'Engine Load (%)', 'Engine Torque Mode', 'TPS (%)',
        'Percent Load Curret Speed', 'Fuel Rate (L-Hr)', 'Vehicle Speed',
        'Inj Q Cur (mg-st)', 'Inj Q Tor (mg-st)', 'Boost Pressure (mBar)',
        'Atmospheric Pressure (mBar)', 'Coolant Temperature (*C)',
        'Oil Temperature (*C)', 'Boost Temperature (*C)', 'Oil Pressure (mBar)',
        'Battery Voltage (V)', 'Cam Speed (rpm)', 'Rail Pressure (mBar)',
        'Rail Pressure set (mBar)', 'MU PWM (%)', 'MU Vol (mm3-s)',
        'Torque Rat', 'Torque (Nm)', 'TQ Limit Set', 'Main Injection (mg-st)',
        'Pilot Injection (mg-st)', 'Pos 2 Injector (mg-st)', 'EGR Prop (%)',
        'EGR Pos D (%)', 'EGR Pos A (%)', 'Clutch Switch', 'Brake Switch',
        'Engine Grad (rpm)', 'param1', 'param2','col_no'
]

fig = px.line_mapbox(lat=data['Latitude'], lon=data['Longitude'],
                     mapbox_style = 'open-street-map',zoom=7)

# app.layout = html.Div([
#     dcc.Graph(id="graph", figure=fig),
# ])

date_list = ['ALL','04-05-2021', '05-05-2021', '06-05-2021', '07-05-2021']
# date_list.append('ALL')
print(date_list)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🚗", className="header-emoji"),
                html.H1(
                    children="Automobile Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of automobile"
                    " and its different features",
                    className="header-description",
                ),
            ],
            className="header",
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Select Feature", className="menu-title"),
                        dcc.Dropdown(
                            id="feature-filter",
                            options=[
                                {"label": col_name, "value": col_name}
                                for col_name in name[3:-3]
                            ],
                            value="RPM",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                # html.Div(
                #     children=dcc.Graph(
                #         id="volume-chart", config={"displayModeBar": False},
                #     ),
                #     className="card",
                # ),

            ],
            className="wrapper",
        ),

        html.Div(
                children=[
                html.Div(children="Date Picker", className="menu-check-title"),
                    dcc.Dropdown(
                        id="date-filter",
                        options=[
                            {"label": date_name, "value": date_name}
                            for date_name in date_list
                        ],
                        value="04-05-2021",
                        clearable=False,
                        searchable=False,
                        className="dropdown",
                    ),
                ],
                 className="menu-check",
            ),

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="graph-make", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                # html.Div(
                #     children=dcc.Graph(
                #         id="volume-chart", config={"displayModeBar": False},
                #     ),
                #     className="card",
                # ),

            ],
            className="wrapper",
        ),



    ]
)


@app.callback(
    [Output("price-chart", "figure"), Output("graph-make", "figure")],
    [
        Input("feature-filter", "value"),
        Input("date-filter", "value"),
        # Input("date-range", "start_date"),
        # Input("date-range", "end_date"),
    ],
)
def update_charts(col_name, date_name):
    # mask = (
    #     (data.region == region)
    #     & (data.type == avocado_type)
    #     & (data.Date >= start_date)
    #     & (data.Date <= end_date)
    # )
    if date_name != 'ALL':
        filtered_data = data[(data['Date']) == date_name]
    else:
        filtered_data = data    
    # print(filtered_data.isnull().sum())
    price_chart_figure = {
        "data": [
            {
                "x": data['Date'],
                "y": data[col_name],
                #"type": "lines",
                # "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": col_name,
                # "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            # "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }


    graph_chart_figure ={
        'data': [
            {
              'hovertemplate': 'lat=%{lat}<br>lon=%{lon}<extra></extra>',
              'lat': filtered_data['Latitude'],
              'legendgroup': '',
              'line': {'color': '#636efa'},
              'lon': filtered_data['Longitude'],
              'mode': 'lines',
              'name': '',
              'showlegend': False,
              'subplot': 'mapbox',
              'type': 'scattermapbox'
              },
            ],

        'layout': {'legend': {'tracegroupgap': 0},
                   'mapbox': {'center': {'lat': 19.144330894574495, 'lon': 73.92980394032968},
                              'domain': {'x': [0.0, 1.0], 'y': [0.0, 1.0]},
                              'style': 'open-street-map',
                              'zoom': 7},
                   'margin': {'t': 60},
                   # 'template': '...'
                },
            }


    # volume_chart_figure = {
    #     "data": [
    #         {
    #             "x": filtered_data["Date"],
    #             "y": filtered_data["Total Volume"],
    #             "type": "lines",
    #         },
    #     ],
    #     "layout": {
    #         "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
    #         "xaxis": {"fixedrange": True},
    #         "yaxis": {"fixedrange": True},
    #         "colorway": ["#E12D39"],
    #     },
    # }
    return price_chart_figure, graph_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)

        # dcc.Graph(config={"displayModeBar": False},
        #     figure={
        #         "data": [
        #             {
        #                 "x": data["Date"],
        #                 "y": data["Engine Load (%)"],
        #                 "type": "lines",
        #             },
        #         ],
        #         "layout": {"title": "Engine Load"},
        #     },
        # id="my-graph", className="wrapper"
        # ),