from dash import callback, Input, Output, State, no_update
import plotly.express as px
from imblearn.over_sampling import SMOTE

import pandas as pd

@callback(
    Output("dataset-table", "data", allow_duplicate=True),
    Input("dataset-store", "data"),
    prevent_initial_call='initial_duplicate'
)
def update_table(data):
    return data


@callback(
    Output("dataset-table", "data", allow_duplicate=True),
    State("dataset-store", "data"),
    Input("column-selector", "value"),
    prevent_initial_call='initial_duplicate'
)
def update_table_columns(data, selected_columns):
    if not selected_columns:
        return data
    df = pd.DataFrame(data)
    return df[selected_columns].to_dict(orient="records")

# Das ist der Callback, um die Tabelle zu laden und zu aktualisieren


@callback(
    [Output("dataset-store", "data"),
     Output("column-selector", "options"),
     Output("target-selector", "options")],
    Input("file-dropdown", "value"),
)
def load_dataset(filepath):
    # gib das dataset, das gerade geladen wurde als Tabelle zurück
    if not filepath:
        return no_update
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records"), df.columns, df.columns


@callback(
    Output("target-distribution", "figure"),
    State("dataset-store", "data"),
    Input("target-selector", "value"),
)
def show_distribution_histogram(data, target):
    if not all([data, target]):
        return no_update
    # gib das dataset, das gerade geladen wurde als Tabelle zurück
    fig = px.histogram(data, x=target)
    return fig


@callback(
    Output("balanced-distribution", "figure"),
    [State("dataset-store", "data"),
    State("column-selector", "value"),
     State("target-selector", "value")],
    Input("balancing-selector", "value"),
)
def balancing_selector(data, selected_features, target, method):
    if not all([data, target, selected_features]):
        return no_update
    data = pd.DataFrame(data).dropna()
    
    sm = SMOTE(random_state=42, k_neighbors=2)
    X_res, y_res = sm.fit_resample(data[selected_features], data[target])
    
    # gib das dataset, das gerade geladen wurde als Tabelle zurück
    fig = px.histogram(y_res)
    return fig
