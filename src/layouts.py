from dash import dcc, html

def get_layout(data):
	return html.Div(
		children=[
			html.Div(
					children=[
					html.P(children="🥑", className="header-emoji"),
					html.H1(
							children="Avocado Analytics", className="header-title"
						),
					html.P(
						children=(
							"Analyze the behavior of avocado prices and the number"
							" of avocados sold in the US between 2015 and 2018"
						),
						className="header-description",
					),
				],
				className="header",
			),
			html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "scatter",
                                    "mode": "lines",
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
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
				html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Total Volume"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Avocados Sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
			],
			className="wrapper",
			),
		],
	)