import pandas as pd
from dash import Dash
from src.layouts import get_layout

data = (
pd.read_csv("avocado.csv")
.query("type == 'conventional' and region == 'Albany'")
.assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
.sort_values(by="Date")
)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"



app.layout = get_layout(data)

if __name__ == "__main__":
    app.run(debug=True)