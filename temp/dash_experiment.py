import dash
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_table


# Sample data
# Replace this with your actual data
matrix = np.random.rand(10, 20) * 1000

# Perform PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(matrix)

# Get word names (replace with your actual word names)
word_names = [f"Word_{i}" for i in range(matrix.shape[1])]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure=px.scatter(
                x=pca_result[:, 0],
                y=pca_result[:, 1],
                labels={'x': 'PC1', 'y': 'PC2'},
                title='PCA 2D Scatter Plot',
                custom_data=np.arange(matrix.shape[0])
            )
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
            id='bar-plot',
            figure=go.Figure()
        )
    ], style={'width': '49%', 'display': 'inline-block'})
])

# Update the bar plot based on the selected scatter point
@app.callback(
    Output('bar-plot', 'figure'),
    [Input('scatter-plot', 'selectedData')]
)
def update_bar_chart(selected_data):
    if not selected_data or not selected_data['points']:
        # If no points are selected, show bar plot for all topics
        bar_fig = go.Figure()
        bar_fig.add_trace(go.Bar(x=word_names, y=matrix.mean(axis=0), name='All Topics'))
        bar_fig.update_layout(title='Word Frequencies for All Topics')
    else:
        topic_index = selected_data['points'][0]['pointIndex']
        selected_topic = matrix[topic_index, :]
        # If points are selected, show bar plot for the selected topic
        bar_fig = go.Figure()
        bar_fig.add_trace(go.Bar(x=word_names, y=selected_topic, name=f'Topic {topic_index}'))
        bar_fig.update_layout(title=f'Word Frequencies for Topic {topic_index}')

    return bar_fig

if __name__ == '__main__':
    app.run_server(debug=True)