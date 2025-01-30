# gwen 2.5 coder

import streamlit as st
import altair as alt
from vega_datasets import data

# Load a dataset
source = data.barley()

# Create an Altair bar chart
chart = (
    alt.Chart(source)
    .mark_bar()
    .encode(
        x='year:O',
        y='sum(yield):Q',
        color='site:N'
    )
)

# Display the chart in Streamlit
# test github sync
st.title('Simple Altair Bar Chart')
st.altair_chart(chart, use_container_width=True)