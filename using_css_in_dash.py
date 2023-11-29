from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer=pd.read_csv('fifa_soccer_players.csv')

avg_age = soccer['age'].mean()
avg_height = soccer['height_cm'].mean()
avg_weight = soccer['weight_kg'].mean()

cards=dbc.Row(
    [
        dbc.Col(dbc.Card(
            [
                html.H4("Avg. Age"),
                html.H5(f'{round(avg_age, 1)} years')
            ], 
            body=True, style={'textAlign':'center', 'color':'white'},
            color='lightBlue')),
        dbc.Col(dbc.Card(
            [
                html.H4("Avg. Height"),
                html.H5(f'{round(avg_height, 1)} years')
            ], 
            body=True, style={'textAlign':'center', 'color':'white'},
            color='lightBlue')),
        dbc.Col(dbc.Card(
            [
                html.H4("Avg. Weight"),
                html.H5(f'{round(avg_weight, 1)} years')
            ], 
            body=True, style={'textAlign':'center', 'color':'white'},
            color='lightBlue')),
    ]
)

app=Dash(external_stylesheets=[dbc.themes.GRID,dbc.themes.BOOTSTRAP])

navbar=dbc.NavbarSimple(
    brand='Soccer Players Dashboard',
    children=[
        html.Img(src='https://www.dreamstime.com/royalty-free-stock-photography-soccer-ball-2-image3282947', height=20),
        html.A('Data Source', href='https://sofifa.com',
        target='_blank',
        style={'color':'black'})
    ],color='primary',fluid=True
)


app.layout=html.Div([
    html.Div(navbar),
    html.Br(),
    cards,
    html.H1('Soccer Players Dashboard'),
    dbc.Row([
    dbc.Col(html.P(['Source: ', 
            html.A('Sofifa', href='https://sofifa.com', target='_blank')]
            )),
    dbc.Col([html.Label('Player name: '),
    dcc.Dropdown(
        options=soccer['long_name'].unique(),
        value=soccer['long_name'].unique()[0]
    )
])])])


if __name__ == '__main__': 
    app.run_server(debug=True)
