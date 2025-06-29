
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import seaborn as sns

# Load dataset
df = sns.load_dataset('titanic')

# Clean dataset
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Titanic Dashboard"),
    dcc.Dropdown(
        id='feature',
        options=[
            {'label': 'Sex', 'value': 'sex'},
            {'label': 'Pclass', 'value': 'pclass'}
        ],
        value='sex'
    ),
    dcc.Graph(id='survival-graph')
])

@app.callback(
    Output('survival-graph', 'figure'),
    Input('feature', 'value')
)
def update_graph(feature):
    fig = px.histogram(df, x=feature, color='survived', barmode='group',
                       labels={'survived': 'Survived'},
                       title=f'Survival by {feature.capitalize()}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
