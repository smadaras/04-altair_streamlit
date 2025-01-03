import streamlit as st
import pandas as pd
import altair as alt

# Streamlit app title
st.title("Altair Graph in Streamlit")

# Create sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

# Display the dataframe
st.write("### Sample Data", data)

# Create an Altair chart
chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Values',
    color='Category'
).properties(
    title="Bar Chart Example"
)

# Display the Altair chart in Streamlit
st.altair_chart(chart, use_container_width=True)