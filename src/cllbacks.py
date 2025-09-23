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
        # ...