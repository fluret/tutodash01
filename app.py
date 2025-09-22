import pandas as pd
from dash import Dash
from src.layouts import get_layout

data = (
pd.read_csv("avocado.csv")
.query("type == 'conventional' and region == 'Albany'")
.assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
.sort_values(by="Date")
)

app = Dash(__name__)



app.layout = get_layout(data)

if __name__ == "__main__":
    app.run(debug=True)