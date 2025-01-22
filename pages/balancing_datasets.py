import dash
from dash import dcc, callback

# import glob oder import os


from dash import html

dash.register_page(__name__)

# Hier kommen die Dataset names rein 
regression_dropdown = dcc.Dropdown(
    id='regression-dropdown',
    options=[
        {'label': 'Support Vector Regression (SVR)', 'value': 'svr'},
        {'label': 'Decision Tree Regression (DTR)', 'value': 'dtr'},
        {'label': 'Linear Regression', 'value': 'linear'}
    ],
    value='linear'
)

# hier wird das Datasets angezeigt. 
# Neben Dash Table gibt es auch andere tabellen, die möglich wären
dataset = dash.dash_table(
    
)


layout = [
    regression_dropdown
]


# Das ist der Callback, um die Tabelle zu laden und zu aktualisieren
@callback(
    
)
def load_dataset (...):
    # gib das dataset, das gerade geladen wurde als Tabelle zurück
    return ...

