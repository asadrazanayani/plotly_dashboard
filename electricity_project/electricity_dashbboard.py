from dash import Dash, html, dcc, dash_table, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

electricity = pd.read_csv('electricity.csv')
min_year = electricity['Year'].min()
max_year = electricity['Year'].max()

app=Dash(external_stylesheets=[dbc.themes.SOLAR])
app.layout=html.Div([
    html.H1('Electricity Prices By US State'),
    dcc.RangeSlider(
        id='year-slider',
        min=min_year,
        max=max_year,
        value=[min_year, max_year],
        marks={i:str(i) for i in range(min_year, max_year+1 )}
    ),
    dcc.Graph(id='map-graph'),
    dash_table.DataTable(
        id='price-info')
])

@app.callback(
    Output('map-graph', 'figure'),
    Input('year-slider', 'value')
)
def update_map_graph(selected_years):
    filtered_electricity = electricity[(electricity['Year']>=selected_years[0]) & (electricity['Year']<=selected_years[1])]
    avg_price_electricity=filtered_electricity.groupby('US_State')['Residential Price'].mean().reset_index()
    map_fig=px.choropleth(avg_price_electricity,locations='US_State',locationmode='USA-states',color='Residential Price',scope='usa',color_continuous_scale='blues')
    return map_fig
    
@app.callback(
    Output('price-info', 'data'),
    Input('map-graph', 'clickData'),
    Input('year-slider', 'value')
)
def update_data_table(clicked_data, year_slider):
    if clicked_data is None:
        return []
    else:
        year_min = round(year_slider[0])
        year_max = round(year_slider[1])
        state = clicked_data['points'][0]['location']
        filtered_electricity=electricity[(electricity['US_State']==state) &
                                        (electricity['Year'] >= year_min) & 
                                        (electricity['Year'] <= year_max)]
        return filtered_electricity.to_dict('records')
    

if __name__ == '__main__':
    app.run_server(port=os.environ.get('port', 8000), debug=True)