import streamlit as st
from datetime import timedelta, datetime
from src.utils.fetch_url import fetch_url
from src.utils.load_data import load_data
import plotly.io as pio
import plotly.express as px
from plotly import graph_objs as go
from plotly.subplots import make_subplots
import plotly


@st.cache
def plot_state(df, state):
    fig = make_subplots(3,1, subplot_titles=["Top 10 Confirmed Cities",
                                             "Top 10 Deaths Cities",
                                             "Top 10 Active Cities"])
    df = df[df["Province_State"] == state]
    df.rename(columns={"Admin2": "City"}, inplace=True)
    df = df.groupby(["City"]).agg({"Confirmed": "sum",
                                   "Deaths": "sum",
                                   "Active": "sum"})
    colors = px.colors.qualitative.Prism
    fig.append_trace(go.Bar(y=df["Confirmed"].nlargest(10).index,
                            x=df["Confirmed"].nlargest(10),
                            orientation='h',
                            marker=dict(color=colors),
                            hovertemplate='<br>Count: %{x:,.2f}',
                            text=df["Confirmed"].nlargest(10),
                            texttemplate="%{text: .3s}",
                            textposition="inside"
                            ),
                     row=1, col=1)
    fig.append_trace(go.Bar(y=df["Deaths"].nlargest(10).index,
                            x=df["Deaths"].nlargest(10),
                            orientation='h',
                            marker=dict(color=colors),
                            hovertemplate='<br>Count: %{x:,.2f}',
                            text=df["Confirmed"].nlargest(10),
                            texttemplate="%{text: .3s}",
                            textposition="inside"
                            ),
                     row=2, col=1)

    fig.append_trace(go.Bar(y=df["Active"].nlargest(10).index,
                            x=df["Active"].nlargest(10),
                            orientation='h',
                            marker=dict(color=colors),
                            hovertemplate='<br>Count: %{x:,.2f}',
                            text=df["Confirmed"].nlargest(10),
                            texttemplate="%{text: .3s}",
                            textposition="inside"
                            ),
                     row=3, col=1)
    fig.update_yaxes(ticks="inside", autorange="reversed")
    fig.update_xaxes(showgrid=False)
    fig.update_traces(opacity=0.7,
                      marker_line_color='rgb(255, 255, 255)',
                      marker_line_width=2.5
                      )
    fig.update_layout(height=1200, width=800,
                      showlegend=False)

    return fig


@st.cache
def state_summary(df, state):
    df = df[df["Province_State"] == state]
    fig = go.Figure()
    colors = px.colors.qualitative.D3
    fig.add_trace(go.Bar(x=df[["Confirmed", "Deaths", "Active"]].columns.tolist(),
                         y=df[["Confirmed", "Deaths", "Active"]].sum().values,
                         text=df[["Confirmed", "Deaths", "Active"]].sum().values,
                         marker=dict(color=[colors[1], colors[3], colors[2], colors[0]]),
                         ),
                  )
    fig.update_traces(opacity=0.7,
                      textposition=["inside", "outside", "inside"],
                      texttemplate='%{text:.3s}',
                      hovertemplate='Status: %{x} <br>Count: %{y:,.2f}',
                      marker_line_color='rgb(255, 255, 255)',
                      marker_line_width=2.5
                      )
    fig.update_layout(
        title="Total count",
        width=800,
        height=600,
        legend_title_text="Status",
        yaxis=dict(title="Count"),
        xaxis=dict(showgrid=False, showticklabels=True),
    )

    return fig


def main():
    st.title("Dashboard")
    pio.templates.default = "plotly_dark"
    date = datetime.today()
    DATA_URL = ""
    df = None
    while True:
        try:
            df = load_data(fetch_url(date))
        except:
            date = date - timedelta(days=1)
            continue
        break
    df = df[df["Country_Region"] == "US"]
    state = st.sidebar.selectbox("Choose state", sorted(df["Province_State"].unique().tolist()))
    st.subheader(state)
    viz = st.selectbox("Choose visualization", ["Summary", "Top Cities"])
    if viz == "Summary":
        st.plotly_chart(state_summary(df, state))
    elif viz == "Top Cities":
        st.plotly_chart(plot_state(df, state))
