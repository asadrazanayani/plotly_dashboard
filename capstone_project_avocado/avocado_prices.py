from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app=Dash()

df = pd.read_csv('data/avocado.csv')
regions = df['region'].unique()
df.drop('Unnamed: 0', axis=1, inplace=True)
df = df.sort_values(by=['Date', 'type'])

@app.callback(
    Output('region_selected', 'children'),
    Output('avocado-price-graph', 'figure'),
    Input('select-region','value')
)
def update_region(region):
    filtered_prices = df[df['region']==region]
    line_fig = px.line(filtered_prices, x=filtered_prices['Date'], y=filtered_prices['AveragePrice'], color='type')
    return f'Avocado Prices in {region}', line_fig

app.layout=html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    html.Br(),
    dcc.Dropdown(id='select-region', options=regions, value=regions[0]),
    html.P(id='region_selected'),
    dcc.Graph(id='avocado-price-graph')
    
    
    

]
)

if __name__ == '__main__':
    print("Initializing")
    app.run_server(debug=True)