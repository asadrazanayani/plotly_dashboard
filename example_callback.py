from dash import Dash, Input, Output, html, dcc

app=Dash()

input_text = dcc.Input(id='unique_input_text', value='Change this', type='text')
output_text = html.Div(id='unique_output_text')
app.layout=html.Div([input_text
    ,output_text
])

@app.callback(
    Output(component_id='unique_output_text',component_property='children'),
    Input(component_id='unique_input_text', component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'

if __name__ == '__main__':
    print("Initializing Dashboard")
    app.run_server(debug=True)
