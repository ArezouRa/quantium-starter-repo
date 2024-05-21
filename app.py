import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# the path to the formatted data file
DATA_PATH = "./formatted_data.csv"

# load in data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# Create options for the radio button
region_options = [
    {"label": "North", "value": "north"},
    {"label": "East", "value": "east"},
    {"label": "South", "value": "south"},
    {"label": "West", "value": "west"},
    {"label": "All", "value": "All"},
]

# create the radio button
radio_button = dcc.RadioItems(
    id="region-filter",
    options=region_options,
    value="All",  # default value
    labelStyle={"display": "inline-block", "margin-right": "10px"},
)

# create the visualization with default settings
line_chart = px.line(
    data, x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales"
)

visualization = dcc.Graph(id="visualization", figure=line_chart)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={"text-align": "center"}
)

# define the app layout
dash_app.layout = html.Div([header, radio_button, visualization])


# define callback to update the visualization based on the selected region
@dash_app.callback(Output(
        "visualization",
        "figure"),
        [Input("region-filter", "value")]
)
def update_figure(selected_region):
    """
    Update the sales line chart based on the selected region.

    Parameters:
    - selected_region (str): The region selected from the radio button.
                             If "All", display data for all regions.

    Returns:
    - line_fig (plotly.graph_objects.Figure): The updated line chart figure.
    """
    if selected_region != "All":
        filtered_data = data[data["region"] == selected_region]
        line_fig = px.line(
            filtered_data,
            x="date",
            y="sales",
            color="region",
            title=f"Pink Morsel Sales - {selected_region.capitalize()}",
        )
    else:
        line_fig = px.line(
            data, x="date",
            y="sales",
            color="region",
            title="Pink Morsel Sales"
        )

    # Update trace colors using update_traces method
    colors = {
        "north": "#02353C",
        "east": "#449342",
        "south": "#2EAF7D",
        "west": "#3A461F",
    }
    for i, trace in enumerate(line_fig.data):
        trace_name = trace.name
        trace_color = colors.get(trace_name, "#008e43")  # Default color
        line_fig.update_traces(
            line=dict(color=trace_color),
            selector=dict(name=trace_name)
        )

    return line_fig


# this is only true if the module is executed as the program entrypoint
if __name__ == "__main__":
    dash_app.run_server(debug=True)
