from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px

happiness=pd.read_csv('world_happiness.csv')
region = happiness['region'].unique()
country = happiness['country'].unique()
rank_score = happiness.columns[2:4]

# line_fig=px.line(happiness[happiness['country']=='United States'],x='year', y='happiness_score',title='Happiness Score In the USA')



app=Dash()

@app.callback(
    Output('country_dropdown','options'),
    Output('country_dropdown','value'),
    Input('region_checklist', 'value')
)
def select_region(region_checklist):
    filtered_happiness = happiness[happiness['region']==region_checklist]
    country_option = filtered_happiness['country'].unique()
    return country_option, country_option[0]

    


@app.callback(
    Output(component_id='happiness-graph', component_property='figure'),
    Output(component_id='average_div', component_property='children'),
    Input('submit-button','n_clicks'),
    # Change the Input to State, now the above input will trigger the function (state below)
    State(component_id='country_dropdown', component_property='value'),
    State(component_id='score_rank', component_property='value')
)

def change_happiness_graph(button_click,country_selected, score_or_rank):
    filtered_happiness = happiness[happiness['country']==country_selected]
    line_fig = px.line(filtered_happiness,x='year', y=f'{score_or_rank}',title=f'{score_or_rank} In the {country_selected}')
    selected_average = round(filtered_happiness[score_or_rank].astype(float).mean(), 3)
    return line_fig, f'The average for {country_selected} is {selected_average}' 

app.layout=html.Div(children=[
    html.H1(children='World Happiness Dashbard'),
    html.P(['This dashboard shows the happiness score.', html.Br(),
    html.A('World Happiness Report Data Source',
    href='https://worldhappiness.report',target='_blank')]),
    dcc.RadioItems(id='region_checklist', options=region, value=region[0]),
    dcc.Dropdown(id='country_dropdown'),
    dcc.RadioItems(id='score_rank', options=rank_score ,value='happiness_score'),
    html.Br(),
    html.Button(id='submit-button', n_clicks=0, children='Update the output'),
    dcc.Graph(id='happiness-graph'),
    html.Div(id='average_div')
])

if __name__ == '__main__':
    app.run_server(debug=True)