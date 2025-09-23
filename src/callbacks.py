from dash import Input, Output

def register_callbacks(app, data):
    @app.callback(
        Output("price-chart", "figure"),
        Output("volume-chart", "figure"),
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    )
    def update_charts(region, avocado_type, start_date, end_date):
        filtered_data = data.query(
            "region == @region and type == @avocado_type"
            " and Date >= @start_date and Date <= @end_date"
        )
        
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["AveragePrice"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Average Price of Avocados",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
        
        volume_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Total Volume"],
                    "type": "lines",
                },
            ],
            "layout": {
                "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
                "xaxis": {"fixedrange": True},
                "yaxis": {"fixedrange": True},
                "colorway": ["#E12D39"],
            },
        }
        
        return price_chart_figure, volume_chart_figure