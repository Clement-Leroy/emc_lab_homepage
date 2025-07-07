import dash
from dash import dcc, ctx, html, Input, Output, State, no_update
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_auth

USERNAME_PASSWORD_PAIRS = [['username','password']]

external_scripts = ["https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js",
                    "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js",
                    'https://trentrichardson.com/examples/timepicker/jquery-ui-timepicker-addon.js']

external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://code.jquery.com/ui/1.13.3/themes/base/jquery-ui.css']

app = dash.Dash(__name__, include_assets_files=True, external_scripts=external_scripts, external_stylesheets=external_stylesheets)
app.secret_key = 'super secret key'
app.title = "MPS | EMC Lab Ettenheim Homepage"
app._favicon = ("icon_MPS.ico")
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server
server.config.update(SECRET_KEY="SECRET_KEY")

# Header
logo=html.Img(src="https://community.element14.com/e14/assets/main/mfg-group-assets/monolithicpowersystemsLogo.png",style={'height': '50px','margin-right':'10px'})
title=html.H1("EMC Lab Homepage",style={'font-size':50,'font-weight':'bold'})
location=html.H1("EMC Lab Ettenheim",style={'font-size':50,'font-weight':'bold'})
header = html.Div([
            html.Div([
                logo
            ], style={'display': 'flex', 'align-items': 'center'}),
            title
        ], style={'display': 'flex', 'justify-content': 'space-between', 'padding': '10px 20px', 'background-color': '#1E2A38', 'color': 'white', 'margin-bottom': '20px', "z-index": "1001"})

# Footer
footer=html.Footer([html.P('Copyright © 2025 Monolithic Power Systems, Inc. All rights reserved.',style={'text-align':'center','color':'#666'})],style={'position':'relative','bottom':'0','width':'100%','padding':'20px 0px','background-color':'#e0e0e0','text-align':'center','margin-top':'20px',"z-index": "1000",})

page = dbc.Col([
    html.Div(html.Label('Test', style={'font-weight':'bold'}))
])

test_column = dbc.Stack([
    html.Link()
])

data_visualization_column = dbc.Stack([
    html.Link()
])

lab_management_column = dbc.Stack([
    html.A(children='EMC Lab | Inventory', href="http://10.10.150.118:8888/", target='_blank', style={'font-weight':'bold', 'font-size':20}),
    html.A(children='EMC Lab | Project Management', href="http://10.10.150.118:8001/", target='_blank', style={'font-weight':'bold', 'font-size':20}),
    html.A(children='EMC Lab | Energy', href="http://10.10.150.118:8050/", target='_blank', style={'font-weight':'bold', 'font-size':20}),
], gap=3)

page = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div([html.Label('Automatized Test', style={'margin-left':20, 'font-weight':'bold', 'font-size':32}), html.Hr(style={'marginTop':'10px', 'marginBottom':'20px', 'width':'600px'}), test_column])),
                dbc.Col(html.Div([html.Label('Data Visualization', style={'margin-left':20, 'font-weight':'bold', 'font-size':32}), html.Hr(style={'marginTop':'10px', 'marginBottom':'20px', 'width':'600px'}), data_visualization_column])),
                dbc.Col(html.Div([html.Label('EMC Lab Management', style={'margin-left':20, 'font-weight':'bold', 'font-size':32}), html.Hr(style={'marginTop':'10px', 'marginBottom':'20px', 'width':'600px'}), lab_management_column])),
            ]
        ),
    ], style = {'padding':'20px'}
)


layout = html.Div([

        html.Div([
            dcc.Store(id='project_number', data=None),
            header,
            html.Div(
                [page], id='project_list_tab',
                style={'flex':'1', 'display': 'block', 'margin-left': 20, 'margin-right': 20}),
            footer,

        ], style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh'})
    ]
    )

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8000)