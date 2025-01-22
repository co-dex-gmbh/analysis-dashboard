import dash
from dash import dcc, callback, Input, Output, dash_table

# import glob oder import os


from dash import html
import pandas as pd

from utils.file_handlers import read_filenames

dash.register_page(__name__)


# Hier kommen die Dataset names rein 
file_dropdown = dcc.Dropdown(
    id='file-dropdown',
    options= read_filenames("data"),
    value='linear'
)

# hier wird das Datasets angezeigt. 
# Neben Dash Table gibt es auch andere tabellen, die möglich wären
dataset = dash_table.DataTable(
    id="dataset-table"
)


layout = [
    file_dropdown,
    dataset
]


# Das ist der Callback, um die Tabelle zu laden und zu aktualisieren
@callback(
    Output("dataset-table", "data"),
    Input("file-dropdown", "value"),
    prevent_initial_call=True
)
def load_dataset (filepath):
    # gib das dataset, das gerade geladen wurde als Tabelle zurück
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")

