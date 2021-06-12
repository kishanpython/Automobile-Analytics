import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import plotly.express as px

data = pd.read_csv("truck1.csv")
data = data.ffill().bfill()


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


date_list = ['ALL','04-05-2021', '05-05-2021', '06-05-2021', '07-05-2021']

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🚗", className="header-emoji"),
                html.H1(
                    children="Automobile Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of vehicles"
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
    ],
)
def update_charts(col_name, date_name):

    if date_name != 'ALL':
        filtered_data = data[(data['Date']) == date_name]
    else:
        filtered_data = data    

    price_chart_figure = {
        "data": [
            {
                "x": data['Date'],
                "y": data[col_name],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {
                "text": col_name,
                # "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
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

    return price_chart_figure, graph_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)