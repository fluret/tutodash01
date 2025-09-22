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
			dcc.Graph(
				figure={
					"data": [
						{
							"x": data["Date"],
							"y": data["AveragePrice"],
							"type": "lines"
						},
					],
					"layout": {"title": "Average Price of Avocados in Albany"},
				},
			),
			dcc.Graph(
				figure={
					"data": [
						{
							"x": data["Date"],
							"y": data["Total Volume"],
							"type": "lines",
						},
					],
					"layout": {"title": "Total Volume of Avocados Sold in Albany"},
				},
			),
		],
	)