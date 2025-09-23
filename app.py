import pandas as pd
from dash import Dash
from src.layouts import get_layout
from src.callbacks import register_callbacks

data = (
    pd.read_csv("avocado.csv", parse_dates=["Date"])
    .sort_values(by="Date")
)

regions = data["region"].drop_duplicates().sort_values().tolist()
avocado_types = data["type"].drop_duplicates().sort_values().tolist()

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"



app.layout = get_layout(data, regions, avocado_types)

register_callbacks(app, data)

if __name__ == "__main__":
    app.run(debug=True)