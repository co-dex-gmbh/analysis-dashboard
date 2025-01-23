import dash
from dash import dcc, dash_table

# import glob oder import os

from utils.file_handlers import read_filenames
from callbacks import balancing_datasets

dash.register_page(__name__)


# Hier kommen die Dataset names rein 
file_dropdown = dcc.Dropdown(
    id='file-dropdown',
    options= read_filenames("data")
)

# hier wird das Datasets angezeigt. 
# Neben Dash Table gibt es auch andere tabellen, die möglich wären
dataset = dash_table.DataTable(
    id="dataset-table",
    page_size=10
)

column_selector = dcc.Dropdown(
    id='column-selector',
    multi=True,
    # options=
)

target_selector = dcc.Dropdown(
    id='target-selector',
    # multi=True,
    # options=
)

balancing_selector = dcc.Dropdown(
    id='balancing-selector',
    options=["smote"]
)

target_distribution = dcc.Graph(id="target-distribution")
balanced_distribution = dcc.Graph(id="balanced-distribution")

dataframe_store = dcc.Store(id="dataset-store")

layout = [
    dataframe_store, 
    file_dropdown,
    column_selector,
    target_selector, 
    dataset,
    target_distribution,
    balancing_selector,
    balanced_distribution
]


