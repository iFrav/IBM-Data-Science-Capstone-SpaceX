import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"

df = pd.read_csv(DATA_URL)
app = Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"

sites = sorted(df["Launch Site"].dropna().unique().tolist())
min_payload = int(df["Payload Mass (kg)"].min())
max_payload = int(df["Payload Mass (kg)"].max())

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={"textAlign": "center"}),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": "All Sites", "value": "ALL"}] +
                [{"label": s, "value": s} for s in sites],
        value="ALL",
        clearable=False,
    ),
    dcc.RangeSlider(
        id="payload-slider",
        min=min_payload,
        max=max_payload,
        step=1000,
        value=[min_payload, max_payload],
        marks={min_payload: str(min_payload), max_payload: str(max_payload)},
    ),
    dcc.Graph(id="success-pie-chart"),
    dcc.Graph(id="success-payload-scatter-chart"),
])

@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value"),
)
def update_pie(site):
    if site == "ALL":
        grouped = df.groupby("Launch Site", as_index=False)["class"].mean()
        return px.bar(grouped, x="Launch Site", y="class",
                      title="Landing Success Rate by Launch Site",
                      labels={"class": "Success rate"})

    filtered = df[df["Launch Site"] == site]
    counts = filtered["class"].value_counts().rename_axis("class").reset_index(name="count")
    counts["Outcome"] = counts["class"].map({1: "Success", 0: "Failure"})
    return px.pie(counts, values="count", names="Outcome",
                  title=f"Landing Outcomes - {site}")

@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")],
)
def update_scatter(site, payload_range):
    low, high = payload_range
    filtered = df[df["Payload Mass (kg)"].between(low, high)]
    if site != "ALL":
        filtered = filtered[filtered["Launch Site"] == site]
    return px.scatter(
        filtered,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        hover_data=["Launch Site"],
        title="Payload Mass vs Landing Outcome",
        labels={"class": "Landing success (1=yes, 0=no)"},
    )

if __name__ == "__main__":
    app.run(debug=True)
